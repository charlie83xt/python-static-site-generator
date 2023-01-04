from ssg.site import Site
import ssg.parsers
import typer

def main(source= "content", dest= "dist"):
    config = {
        "source": source,
        "dest": dest,
        parsers: [ssg.parsers.ResourceParsers()]
    }

    site = Site(**config).build()

typer.run(main)