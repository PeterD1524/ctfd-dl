import argparse
import ast
import dataclasses
import pathlib
from collections.abc import Iterable, Sequence

import ctfd_dl.exceptions


def eq(a, b):
    if type(a) is not type(b):
        return False
    if (isinstance(a, str) and isinstance(b, str)) or (
        isinstance(a, bool) and isinstance(b, bool)
    ):
        return a == b
    elif isinstance(a, ast.AST) and isinstance(b, ast.AST):
        iterator = zip(ast.iter_fields(a), ast.iter_fields(b), strict=True)
        while True:
            try:
                (field_name_a, value_a), (field_name_b, value_b) = next(iterator)
            except ValueError:
                return False
            except StopIteration:
                return True
            if field_name_a != field_name_b:
                return False
            if not eq(value_a, value_b):
                return False
    elif isinstance(a, list) and isinstance(b, list):
        iterator = zip(a, b, strict=True)
        while True:
            try:
                value_a, value_b = next(iterator)
            except ValueError:
                return False
            except StopIteration:
                return True
            if not eq(value_a, value_b):
                return False
    elif a is None and b is None:
        return True
    else:
        raise ctfd_dl.exceptions.Error((a, b))


def fields(stmts: Iterable[ast.stmt]):
    for stmt in stmts:
        if not isinstance(stmt, ast.Assign):
            continue
        if len(stmt.targets) != 1:
            continue
        target = stmt.targets[0]
        if not isinstance(target, ast.Name):
            continue
        id = target.id
        if not eq(target.ctx, ast.Store()):
            raise ctfd_dl.exceptions.Error
        value = stmt.value
        if not isinstance(value, ast.Call):
            continue
        if not eq(
            value.func,
            ast.Attribute(
                value=ast.Name(id="db", ctx=ast.Load()), attr="Column", ctx=ast.Load()
            ),
        ):
            continue
        keywords = value.keywords
        nullable = True
        for keyword in keywords:
            if eq(
                keyword, ast.keyword(arg="primary_key", value=ast.Constant(value=True))
            ) or eq(
                keyword, ast.keyword(arg="nullable", value=ast.Constant(value=False))
            ):
                nullable = False
        arg = value.args[0]
        if eq(
            arg,
            ast.Attribute(
                value=ast.Name(id="db", ctx=ast.Load()), attr="Integer", ctx=ast.Load()
            ),
        ):
            name = ast.Name(id="int", ctx=ast.Load())
        elif (
            eq(
                arg,
                ast.Attribute(
                    value=ast.Name(id="db", ctx=ast.Load()), attr="Text", ctx=ast.Load()
                ),
            )
            or eq(
                arg,
                ast.Attribute(
                    value=ast.Name(id="db", ctx=ast.Load()),
                    attr="DateTime",
                    ctx=ast.Load(),
                ),
            )
            or (
                isinstance(arg, ast.Call)
                and eq(
                    arg.func,
                    ast.Attribute(
                        value=ast.Name(id="db", ctx=ast.Load()),
                        attr="String",
                        ctx=ast.Load(),
                    ),
                )
            )
        ):
            name = ast.Name(id="str", ctx=ast.Load())
        elif eq(
            arg,
            ast.Attribute(
                value=ast.Name(id="db", ctx=ast.Load()), attr="Boolean", ctx=ast.Load()
            ),
        ):
            name = ast.Name(id="bool", ctx=ast.Load())
        elif eq(
            arg,
            ast.Attribute(
                value=ast.Name(id="db", ctx=ast.Load()), attr="JSON", ctx=ast.Load()
            ),
        ):
            name = ast.Name(id="Any", ctx=ast.Load())
        else:
            raise ctfd_dl.exceptions.Error(
                id, "[{}]".format(", ".join(ast.dump(arg) for arg in value.args))
            )
        if nullable:
            name = ast.BinOp(left=name, op=ast.BitOr(), right=ast.Constant(value=None))
        yield id, name


@dataclasses.dataclass
class Definition:
    name: str
    fields: Sequence[tuple[str, ast.expr]]


def definitions(module: ast.Module):
    for node in module.body:
        if not isinstance(node, ast.ClassDef):
            continue
        if not eq(
            node.bases,
            [
                ast.Attribute(
                    value=ast.Name(id="db", ctx=ast.Load()),
                    attr="Model",
                    ctx=ast.Load(),
                )
            ],
        ):
            continue
        yield Definition(name=node.name, fields=tuple(fields(node.body)))


def fields_to_ann_assign(fields: Iterable[tuple[str, ast.expr]]):
    for id, annotation in fields:
        yield ast.AnnAssign(
            target=ast.Name(id=id, ctx=ast.Store()), annotation=annotation, simple=1
        )


def body(definitions: Iterable[Definition]):
    yield ast.Import(names=[ast.alias(name="dataclasses")])
    yield ast.ImportFrom(module="typing", names=[ast.alias(name="Any")], level=0)
    for definition in definitions:
        yield ast.ClassDef(
            name=definition.name,
            bases=[],
            keywords=[],
            body=list(fields_to_ann_assign(definition.fields)),
            decorator_list=[
                ast.Attribute(
                    value=ast.Name(id="dataclasses", ctx=ast.Load()),
                    attr="dataclass",
                    ctx=ast.Load(),
                )
            ],
        )


def main():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("path")
    args = parser.parse_args()
    path = args.path
    if not isinstance(path, str):
        raise ctfd_dl.exceptions.Error
    module = ast.parse(pathlib.Path(path).read_text())
    print(
        ast.unparse(ast.Module(body=list(body(definitions(module))), type_ignores=[]))
    )


if __name__ == "__main__":
    main()
