from site import Site
import typer

def main(source= "content", dest= "dist"):
    config = {
        "source": source,
        "dest": dest
    }

    site = Site(**config).build()

if __name__ == '__main__':
    typer.run(main)