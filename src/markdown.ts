// import fs from 'fs';
import marked from 'marked';

export function getPost(slug: string): string | null {
  try {
    // const fileContent = fs.readFileSync(`./content/${slug}.md`, 'utf-8');
    // return marked(fileContent);
  } catch (error) {
    console.error(`Error reading post: ${slug}`, error);
    return null;
  }
}
