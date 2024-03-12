from app import DevelopmentConfig, create_app

if __name__ == "__main__":
    config = DevelopmentConfig
    create_app().run(debug=config.DEBUG)
