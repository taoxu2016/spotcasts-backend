import scrapy

class PodcastsCollection(scrapy.Spider):
    name = "podcasts_collection"
    start_urls = ["https://www.listennotes.com/best-web-design-podcasts-140/"]

    def parse(self, response):
        cards = response.css("#podcasts .ln-channel-episode-detail-card")

        podcasts = []

        for card in cards:
            data = {}
            data["uuid"] = card.css("div[data-id='channel-toolbar']::attr(data-channel-uuid)").get()
            data["title"] = card.css(".ln-channel-episode-card-info-title a::text").get().strip()
            data["thumbnail"] = card.css("img.ln-channel-image::attr(src)").get()
            data["description"] = card.css(".ln-channel-detailed-card-description::text").get().strip()
            data["author"] = card.css(".ln-channel-episode-card-info-subtitle::attr(title)").get()

            data["latest_episode"] = {
                "title": card.css(".ln-channel-episode-card-body .ln-channel-episode-card-info-title a::text").get().strip(),
                "episode_link": card.css(".ln-channel-episode-card-body .ln-channel-episode-card-info-title a::attr(href)").get(),
                "id": card.css("div[data-type='episode-audio-player']::attr(data-episode-uuid)").get(),
                "published": card.css(".ln-channel-episode-card-info-subtitle time::text").get().strip(),
                "duration": card.css(".ln-episode-timestamp::text").get().strip(),
            }

            podcasts.append(data)

        yield {
            "podcasts": podcasts
        }


