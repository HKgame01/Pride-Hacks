# import and run flask application

from website import create_app 

app = create_app()

if __name__ == '__main__': # only execute if running file not just import
  app.run(debug=True) # for development not production
