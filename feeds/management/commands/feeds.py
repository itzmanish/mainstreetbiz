import feedparser
from feeds.models import FeedUrl, FeedPost
from time import mktime
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = ''
    help = 'Gets N recent blog posts. Better than parsing the list every page load.'

    def add_arguments(self, parser):
        parser.add_argument('number')

    def handle(self, *arg, **options):
        num_blog_posts = int(options['number'])

        feeds = FeedUrl.objects.all()
        for post in FeedPost.objects.all():
            post.delete()

        for i in feeds:
            feed = feedparser.parse(i.site_url)

            loop_max = num_blog_posts if len(
                feed['entries']) > num_blog_posts else len(feed['entries'])

            for i in range(0, loop_max):
                if feed['entries'][i]:
                    blog_post = FeedPost()
                    blog_post.title = feed['entries'][i].title
                    blog_post.link = feed['entries'][i].link
                    blog_post.desc = feed['entries'][i].description
                    blog_post.date = datetime.fromtimestamp(
                        mktime(feed['entries'][i].published_parsed))
                    blog_post.save()
