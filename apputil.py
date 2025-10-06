# Exercise 1 - Creating a class called genius
class Genius:
  def __init__(self, access_token):
      if not access_token:
          raise ValueError("Access token is required")
      self.access_token = access_token