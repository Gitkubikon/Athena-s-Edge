import { getCookieValue, setCookie } from "./shenanigans";

class Api {
  API_BASE_URL: string;
  token: string;

  constructor(API_BASE_URL: string) {
    this.API_BASE_URL = API_BASE_URL;
    this.token = getCookieValue("token");
  }

  private async request(method: string, path: string, data?: any): Promise<{ content?: string }> {
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
    const content = method === 'GET' ? await response.text() : undefined;
    return { content };
  }

  login(username: string, password: string): Promise<boolean> {
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

  get(path: string): Promise<{ content?: string }> {
    return this.request('GET', path);
  }

  post(path: string, data: any): Promise<{ content?: string }> {
    return this.request('POST', path, data);
  }

  put(filename: string): Promise<{ content?: string }> {
    return this.request('PUT', '/content', { filename });
  }

  delete(filename: string): Promise<{ content?: string }> {
    return this.request('DELETE', `/content/${filename}`);
  }
}

export { Api };
