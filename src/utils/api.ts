import { getCookieValue, setCookie } from "./shenanigans";

class Api {
  API_BASE_URL: string;
  token: string;
  METADATA: JSON;

  constructor(API_BASE_URL: string) {
    this.API_BASE_URL = API_BASE_URL;
    this.token = getCookieValue("token");
    this.getMetadata().then((metadata) => {
      this.METADATA = metadata;
    });
  }

  private async request<T>(method: string, path: string, data?: any): Promise<T> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };
    if (this.token) {
      headers['Authorization'] = `Bearer ${this.token}`;
    }
    const body = data ? JSON.stringify(data) : undefined;
    const response = await fetch(`${this.API_BASE_URL}${path}`, {
      method,
      headers,
      body,
    });
    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}: ${response.statusText}`);
    }
    const content = await response.json();
    return content as T;
  }

  async getMetadata(): Promise<JSON> {
    return this.request<JSON>('GET', '/metadata');
  }

  async getContent(path: string): Promise<string | Blob> {
    const response = await this.request<Response>('GET', `/content/${path}`);
    console.log(await response)
    const contentType = response.headers.get('Content-Type');
    if (contentType?.startsWith('text/markdown')) {
      const text = await response.text();
      return text;
    } else if (contentType?.startsWith('image/')) {
      const blob = await response.blob();
      return blob;
    } else if (contentType?.startsWith('video/')) {
      const blob = await response.blob();
      return blob;
    } else {
      throw new Error(`Unsupported content type: ${contentType}`);
    }
  }


  async login(username: string, password: string): Promise<boolean> {
    return fetch(`${this.API_BASE_URL}/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    })
      .then(async (response) => {
        const data = await response.json();
        if (response.ok) {
          const token = data.token;
          setCookie('token', token);
          this.token = token;
          return true;
        } else {
          throw new Error(data.message);
        }
      })
      .catch((error) => {
        console.error(error);
        return false;
      });
  }

  async patch(filename: string, content?: Metadata): Promise<Response> {
    return this.request('PATCH', '/content', { filename, ...content });
  }

  async put(filename: string, content?: Metadata): Promise<Response> {
    return this.request('PUT', '/content', { filename, ...content });
  }

  async delete(filename: string): Promise<Response> {
    return this.request<Response>('DELETE', `/content/${filename}`);
  }
}

interface Metadata {
  main_tag: string;
  cover: string;
  images: string[];
  videos: string[];
  tags: string[];
  popularity: number;
  created_at: string;
  sentiment: {
    polarity: string;
    subjectivity: string;
    emotions: {
      anger: string;
      joy: string;
      fear: string;
      sadness: string;
    };
    sentiment_categories: {
      positive: string;
      negative: string;
      neutral: string;
    };
    sentiment_keywords: string;
  };
  targeting: {
    age_range: {
      min_age: string;
      max_age: string;
    };
    location: {
      country: string;
      city: string;
      region: string;
    };
    interests: string;
    gender: string;
    education_level: string;
    income_level: string;
    occupation: string;
    marital_status: string;
    parental_status: string;
  };
  engagement: {
    views: number;
    likes: number;
    comments: number;
    shares: number;
  };
}

export { Api };
