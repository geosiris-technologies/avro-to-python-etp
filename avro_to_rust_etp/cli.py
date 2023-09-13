# -*- coding: utf-8 -*-

"""Console script for avro_to_rust_etp."""
import os
import sys

import click
from click import Path

from avro_to_rust_etp.reader.read import AvscReader
from avro_to_rust_etp.writer.writer import AvroWriter


PIP_HELP = 'make package pip installable using this name'
AUTHOR_HELP = 'author name of the pip installable package'
VERSION_HELP = 'version of the pip intallable package'
OUT_ONLY_HELP = 'do not generate the lib but only files in "out" template folder. These are supposed to be used in other library (e.g. etpproto)'


@click.command()
@click.argument('source', type=Path(), default=None)
@click.argument('target', type=Path(), default=None)
@click.option('--pip', type=str, default=None, required=False, show_default=True, help=PIP_HELP)  # NOQA
@click.option('--author', type=str, default=None, required=False, show_default=True, help=AUTHOR_HELP)  # NOQA
@click.option('--package_version', type=str, default='0.1.0', required=False, show_default=True, help=VERSION_HELP)  # NOQA
@click.option('--only_out', is_flag=True, required=False, help=OUT_ONLY_HELP)  # NOQA
def main(source, target, pip=None, author=None, package_version=None, only_out=False):
    """avro-to-rust: compile avro avsc schemata to python classes
    """

    if os.path.isfile(source):
        reader = AvscReader(file=source)
    else:
        reader = AvscReader(directory=source)
    reader.read()
    writer = AvroWriter(
        reader.file_tree,
        pip=pip,
        author=author,
        package_version=package_version
    )
    if(only_out):
        writer.write_out(root_dir=target)
    else:
        writer.write(root_dir=target)
    del reader
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
