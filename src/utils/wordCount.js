/**
 * Calculates word count supporting both English and CJK characters.
 */
export function calculateWordCount(text) {
  if (!text) return 0;

  // Strip HTML tags (<br/>, <span>, …) so they are not counted as words
  const cleanText = text
    .replace(/<[^>]*>/g, "")
    .replace(/[#*`_>\[\]\(\)]/g, "");

  // Count alphanumeric English sequences
  const englishWords = (cleanText.match(/[a-zA-Z0-9]+/g) || []).length;

  // Count CJK characters (Chinese, Japanese, Korean)
  const chineseChars = (cleanText.match(/[\u4e00-\u9fa5]/g) || []).length;

  return englishWords + chineseChars;
}
