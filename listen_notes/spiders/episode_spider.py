import scrapy

class PodcastsSpider(scrapy.Spider):
    name = "episode"

    def __init__(self, url="https://www.listennotes.com/podcasts/syntax-tasty-web/voice-coding-is-really-good-qT4WpmPfZKt/"):
        self.start_urls = [url]

    def parse(self, response):
        episode_audio = response.css("#episode-play-button-toolbar::attr(data-audio)").get()
        episode_uuid = response.css("#episode-play-button-toolbar::attr(data-episode-uuid)").get()
        show_notes = response.css(".ln-channel-episode-description-text").extract()

        yield {
            'episode_audio': episode_audio,
            'episode_uuid': episode_uuid,
            'show_notes': show_notes
        }
