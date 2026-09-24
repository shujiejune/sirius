---
title: 'Markdown Style Guide'
description: 'Here is a sample of some basic Markdown syntax that can be used when writing Markdown content in Astro.'
pubDate: 'Feb 14 2026'
updatedDate: 'Feb 27 2026'
heroImage: '../../assets/images/blog-placeholder-1.jpg'
tags: ['markdown', 'style', 'guide']
---

<p>残腊归来绿不凋，得风黑鹄鼓春潮。湖光贯破琉璃冷，草色犹粘上石桥。</p>
<p>殘臘歸來綠不凋，得風黑鵠鼓春潮。湖光貫破琉璃冷，草色猶粘上石橋。</p>

## Headings

The following HTML `<h1>`—`<h6>` elements represent six levels of section headings. `<h1>` is the highest section level while `<h6>` is the lowest.

## Paragraph

In former times, King Goujian of Yue had five precious swords that were renowned throughout the world. There was a guest who could appraise swords; his name was Xue Zhu. The king summoned him and asked, saying, "I have five precious swords. Please allow me to show them to you." Xue Zhu replied, "My understanding is insufficient for such a task, but since the great king has requested it, I dare not refuse." He then summoned the keeper of swords, and the king ordered him to bring out the sword Hecao. Xue Zhu replied, "Hecao is not a precious sword." A precious sword displays five colors together, none of which can surpass the others. "Hecao has already gained a reputation, but it is not a precious sword." The king said, "Bring out Juque." Xue Zhu said, "It is not a precious sword. A precious sword is made by blending gold, tin, and copper without separation among them. Now Juque has already separated; it is not a precious sword." The king said, "Indeed, when Juque was first completed, I was seated on the Lu Tan terrace. A palace attendant with four white deer pulling a carriage passed by. The carriage rushed forward and the deer were startled; I drew my sword to point at them, and all four deer flew upward, vanishing without a trace." "It pierced through copper cauldrons, severed iron ropes, and split things as easily as rice grains; hence it is called Juque." The king took out Chunjun. Upon hearing this, Xue Zhu suddenly seemed defeated. After a while, he looked as if he had come to an understanding. He descended the steps and deeply pondered, then sat quietly with his clothes arranged to gaze at it. With trembling hands he brushed and lifted it; its brilliance burst forth like a lotus just emerging. Observing its blade, the light was dazzling as if stars were aligned in motion; Observing its gleam, it was hazy and flowing like water overflowing from a pond; Observing the cut, it stood firm as if made of solid stone; Observing its quality, it shimmered brilliantly like melting ice. "Is this what is called Chunjun?" The king said, "Yes, it is." "A guest who can appraise it directly would be worth two market towns, a thousand fine horses, and two cities with a thousand households. Would that be acceptable?" Xue Zhu replied, "No." "When this sword was forged, the red mountain of Chi Jin was broken open to extract tin; the stream Ruyue dried up to yield copper; Rain God swept and sprinkled, Thunder God struck the bellows; Jiaolong held up the furnace, while the Heavenly Emperor prepared the charcoal; The Supreme Deity observed from above as celestial essence descended. Ouye then, drawing upon the spirit of heaven and employing all his skill, forged three large weapons and two small ones: first was Zhanlu, second Chunjun, third Shengxia, fourth Yuchang, fifth Juque. During the reign of King Helu of Wu, he obtained three swords: Shengxia, Yuchang, and Zhanlu. King Helu was unjust; when his children died, he killed people to accompany them in death. The sword Zhanlu, like water, departed from Wu and passed through Qin to Chu. The king of Chu awoke from his sleep, obtained King Helu's Zhanlu sword, and thus the leader of Wu was beheaded but survived in name only. The king of Qin heard about it and sought the sword, but failed to obtain it. He then raised an army to attack Chu, saying, "Give me the Zhanlu sword, and I will withdraw my troops from you." The king of Chu did not give it up. At that time, King Helu also used the Yuchang sword to stab King Liao of Wu, causing him to be stripped and killed in three incidents. King Helu sent Zhuanzhu as a fish cook, who drew the sword and stabbed him, thus assassinating King Liao. This was only a small test against an enemy state; its great use in the world had yet to be seen. Now, the red mountain Chi Jin has closed again, and Ruyue stream is deep and unfathomable. The deities no longer descended, and Ouyezi soon died. Even if one were to pour out the wealth of an entire city, drain rivers of pearls and jade, it still would not be enough to obtain this single item. How could two market towns, a thousand superior horses, and two cities of a thousand households even be mentioned!"

## Images

### Syntax

```markdown
![Alt text](./full/or/relative/path/of/image)
```

### Output

![blog placeholder](../../assets/images/blog-placeholder-1.jpg)

## Blockquotes

The blockquote element represents content that is quoted from another source, optionally with a citation which must be within a `footer` or `cite` element, and optionally with in-line changes such as annotations and abbreviations.

### Blockquote without attribution

#### Syntax

```markdown
> Tiam, ad mint andaepu dandae nostion secatur sequo quae.  
> **Note** that you can use _Markdown syntax_ within a blockquote.
```

#### Output

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.  
> **Note** that you can use _Markdown syntax_ within a blockquote.

### Blockquote with attribution

#### Syntax

```markdown
> Don't communicate by sharing memory, share memory by communicating.<br>
> — <cite>Rob Pike[^1]</cite>
```

#### Output

> Don't communicate by sharing memory, share memory by communicating.<br>
> — <cite>Rob Pike[^1]</cite>

[^1]: The above quote is excerpted from Rob Pike's [talk](https://www.youtube.com/watch?v=PAAkCSZUG1c) during Gopherfest, November 18, 2015.

## Tables

### Syntax

```markdown
| Italics   | Bold     | Code   |
| --------- | -------- | ------ |
| _italics_ | **bold** | `code` |
```

### Output

| Italics   | Bold     | Code   |
| --------- | -------- | ------ |
| _italics_ | **bold** | `code` |

## Code Blocks

### Syntax

we can use 3 backticks ``` in new line and write snippet and close with 3 backticks on new line and to highlight language specific syntax, write one word of language name after first 3 backticks, for eg. html, javascript, css, markdown, typescript, txt, bash

````markdown
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Example HTML5 Document</title>
  </head>
  <body>
    <p>Test</p>
  </body>
</html>
```
````

### Output

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Example HTML5 Document</title>
  </head>
  <body>
    <p>Test</p>
  </body>
</html>
```

## List Types

### Ordered List

#### Syntax

```markdown
1. First item
2. Second item
3. Third item
```

#### Output

1. First item
2. Second item
3. Third item

### Unordered List

#### Syntax

```markdown
- List item
- Another item
- And another item
```

#### Output

- List item
- Another item
- And another item

### Nested list

#### Syntax

```markdown
- Fruit
  - Apple
  - Orange
  - Banana
- Dairy
  - Milk
  - Cheese
```

#### Output

- Fruit
  - Apple
  - Orange
  - Banana
- Dairy
  - Milk
  - Cheese

## Other Elements — abbr, sub, sup, kbd, mark

### Syntax

```markdown
<abbr title="Graphics Interchange Format">GIF</abbr> is a bitmap image format.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Press <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>Delete</kbd> to end the session.

Most <mark>salamanders</mark> are nocturnal, and hunt for insects, worms, and other small creatures.
```

### Output

<abbr title="Graphics Interchange Format">GIF</abbr> is a bitmap image format.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Press <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>Delete</kbd> to end the session.

Most <mark>salamanders</mark> are nocturnal, and hunt for insects, worms, and other small creatures.
