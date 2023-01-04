from ssg.site import Site
import ssg.parsers
import typer

def main(parsers, source= "content", dest= "dist"):
    config = {
        "source": source,
        "dest": dest,
        parsers: [ssg.parsers.ResourceParsers()]
    }

    site = Site(**config).build()

typer.run(main)