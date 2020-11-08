import scrapy

class PodcastsSpider(scrapy.Spider):
    name = "podcasts"

    def __init__(self, name):
        self.start_urls = [f'https://www.listennotes.com/podcasts/{name}/']

    def parse(self, response):
        uuid = response.css('#channel-toolbar::attr(data-channel-uuid)').get()
        text = response.xpath('//h1/a/text()').get()
        host = response.css('.ln-channel-header-subtitle a::text').get()
        thumbnail = response.css('.ln-channel-header-card a::attr(href)').get()
        description = response.css('.ln-channel-episode-description-text::text').get().strip()

        latest_episode_card = response.css('.ln-channel-episode-detail-card')

        latest_episode = {
            'title': latest_episode_card.css('.ln-channel-episode-card-info-title a::text').get().strip(),
            'aired_on': latest_episode_card.css('.ln-channel-episode-card-info-subtitle time::text').get().strip(),
            'episode_link': latest_episode_card.css('.ln-channel-episode-card-info-title a::attr(href)').get().strip(),
            'duration': latest_episode_card.css('.ln-episode-timestamp::text').get().strip()
        }

        episode_cards = response.css('.ln-channel-individual-episode-card')

        episodes = []
        for episode_card in episode_cards:
            episode = {
                'title': episode_card.css('.ln-channel-episode-card-info-title a::text').get().strip(),
                'aired_on': episode_card.css('.ln-channel-episode-card-info-subtitle time::text').get().strip(),
                'episode_link': episode_card.css('.ln-channel-episode-card-info-title a::attr(href)').get().strip(),
                'duration': episode_card.css('.ln-episode-timestamp::text').get().strip()
            }

            episodes.append(episode)

        yield {
            'uuid': uuid,
            'text': text,
            'host': host,
            'thumbnail': thumbnail,
            'description': description,
            'latest_episode': latest_episode,
            'previous_episodes': episodes
        }
