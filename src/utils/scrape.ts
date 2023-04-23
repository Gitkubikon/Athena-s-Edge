interface RedditPost {
  title: string;
  score: number;
}

interface HackerNewsPost {
  title: string;
  points: number;
}

interface TwitterTweet {
  text: string;
  retweets: number;
}

interface InstagramPost {
  caption: string;
  likes: number;
}

export async function getPopularRedditTopics(): Promise<RedditPost[]> {
  const response = await fetch('https://www.reddit.com/r/popular.json');
  const data = await response.json();

  if (!data || !data.data || !data.data.children) {
    throw new Error('Invalid Reddit API response.');
  }

  return data.data.children.map((child: any) => ({
    title: child.data.title,
    score: child.data.score,
  }));
}

export async function getPopularHackerNewsPosts(): Promise<HackerNewsPost[]> {
  const response = await fetch('https://hacker-news.firebaseio.com/v0/topstories.json');
  const storyIds = await response.json();

  const topStories = storyIds.slice(0, 10);
  const storyPromises = topStories.map((id: number) =>
    fetch(`https://hacker-news.firebaseio.com/v0/item/${id}.json`).then((response) => response.json())
  );

  const stories = await Promise.all(storyPromises);

  return stories.map((story: any) => ({
    title: story.title,
    points: story.score,
  }));
}

export async function getPopularTweets(): Promise<TwitterTweet[]> {
  const bearerToken = process.env.BEARER_TOKEN;
  const url = 'https://api.twitter.com/2/tweets/search/recent?query=popular&expansions=author_id';
  const headers = {
    'Authorization': `Bearer ${bearerToken}`,
    'Content-Type': 'application/json',
  };
  const response = await fetch(url, { headers });
  const data = await response.json();

  if (!data || !data.data) {
    throw new Error('Invalid Twitter API response.');
  }

  return data.data.map((tweet: any) => ({
    text: tweet.text,
    retweets: tweet.public_metrics.retweet_count,
  }));
}

export async function getPopularInstagramPosts(): Promise<InstagramPost[]> {
  const accessToken = 'YOUR_ACCESS_TOKEN';
  const response = await fetch(`https://graph.instagram.com/me/media?fields=caption,media_type,media_url,thumbnail_url,permalink,like_count&access_token=${accessToken}`);
  const data = await response.json();

  if (!data || !data.data) {
    throw new Error('Invalid Instagram API response.');
  }

  return data.data.map((post: any) => ({
    caption: post.caption,
    likes: post.like_count,
  }));
}

