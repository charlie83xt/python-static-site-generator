from site import Site
from . import typer

def main(source= "content", dest= "dist"):
    config = {
        "source": source,
        "dest": dest
    }

    site = Site(**config).build()

typer.run(main())