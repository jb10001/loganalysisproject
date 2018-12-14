# Log Analysis Code in Python


import psycopg2

DBNAME = "news"

def getTopThreeArticles(): 
  """Return the top three most populus articles from the news 'database', most popular first."""
  db = psycopg2.connect(database="news")
  c = db.cursor()
  c.execute("select count(*) as num, status, path from log group by path, status order by status, num desc;")
  news = c.fetchall()
  db.close()
  return news




def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("insert into posts values (%s)", (bleach.clean(content),))  # good
  db.commit()
  db.close()


print("Hell world")

# MY CODE, HERE

# 2 fUNCTIONS, COPied AND PASTED
def getTopArticleAuthors()
"""Return the top three most populus articles from the news 'database', most popular first."""
  db = psycopg2.connect(database="news")
  c = db.cursor()
  c.execute("select count(*) as num, status, path from log group by path, status order by status, num desc;")
  news = c.fetchall()
  db.close()
  return news


def getDaysWithMoreThanOneLeadErrors()
"""Return the top three most populus articles from the news 'database', most popular first."""
  db = psycopg2.connect(database="news")
  c = db.cursor()
  c.execute("select count(*) as num, status, path from log group by path, status order by status, num desc;")
  news = c.fetchall()
  db.close()
  return news




