from src.minecrafter import create_app
from mongoengine import connect


def main():
    connect('minecrafter')

    app = create_app()
    app.run(debug=True)


if __name__ == '__main__':
    main()
