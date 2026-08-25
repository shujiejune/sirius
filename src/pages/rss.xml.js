import { getCollection } from 'astro:content';
import rss from '@astrojs/rss';
import { SITE_DESCRIPTION, SITE_TITLE } from '../consts';

export async function GET(context) {
	const posts = await getCollection('blog');
	// context.site does not include the configured base path. Build the real
	// origin+base URL, ensuring a trailing slash so relative item links
	// resolve under the base instead of replacing its last path segment.
	const site = new URL(import.meta.env.BASE_URL.replace(/\/+$/, '') + '/', context.site);
	return rss({
		title: SITE_TITLE,
		description: SITE_DESCRIPTION,
		site,
		items: posts.map((post) => ({
			...post.data,
			// No leading slash: resolves relative to the site's base path
			link: `blog/${post.id}/`,
		})),
	});
}
