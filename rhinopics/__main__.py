# -*- coding: utf-8 -*-
"""Entry point of the rhinopics cli."""
import pathlib
import click
import click_pathlib

from .rhinopics import Rhinopics


@click.command()
@click.argument('keyword')
@click.option('--directory', '-d',
              default='./', show_default=True,
              type=click_pathlib.Path(exists=True, file_okay=False,
                                      dir_okay=True, readable=True),
              help='Directory containing the pictures to rename.'
              )
@click.option('--backup', '-b', is_flag=True,
              help='Create copies instead of renaming the files.'
              )
@click.option('--lowercase', '-l', is_flag=True,
              help='Modify the extension to lowercase.'
              )
def main(keyword: str, directory: pathlib.PosixPath, backup: bool, lowercase: bool):
    """Rename all pictures in a directory with a common keyword.

    The date from the metadata of the pictures is retrieved and concanated to the keyword,
    followed by a counter to distinguish pictures taken the same day.

    Parameters
    ----------
    keyword : str
        Common keyword to use when renaming the pictures.
    directory : str, default './'
        Directory containing the pictures to rename, default is the current directory.
    backup : bool, default False
        If flag is present, copy the pictures instead of renaming them.

    Examples
    --------
    $ rhinopics mykeyword
    -> mykeyword_20190621_001
    """
    rhinopics = Rhinopics(directory, keyword, backup, lowercase)
    rhinopics.rename()


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
