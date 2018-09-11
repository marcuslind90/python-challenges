class Solution(object):
    small = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
             "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
             "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
             "Nineteen"]
    teens = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy",
             "Eighty", "Ninety"]
    large = ["", "Thousand", "Million", "Billion"]
    hundred = "Hundred"
    negative = "Negative"

    def convert(self, num):
        """
        Convert number from integer to english language.
        E.g. 192 becomes One Hundred Ninety Two
        """
        if num == 0:
            return self.small[0]
        elif num < 0:
            return "%s %s" % (self.negative, self.convert(-1 * num))

        words = []
        # Keep track on how many thousands that have passed.
        # E.g. Thousand, Million, Billion etc.
        millenials = 0

        while num > 0:
            if num % 1000 != 0:
                chunk = "%s %s" % (
                    self.convertChunk(num % 1000),
                    self.large[millenials]
                )
                words.insert(0, chunk)
            num = num//1000
            millenials += 1

        return ' '.join(words)

    def convertChunk(self, num):
        words = []
        if num >= 100:
            words.append(self.small[num//100])
            words.append(self.hundred)
            num %= 100

        if num >= 10 and num <= 19:
            words.append(self.small[num])
        elif num >= 20:
            words.append(self.teens[num//10])
            num %= 10

        if num >= 1 and num <= 9:
            words.append(self.small[num])

        return ' '.join(words)


s = Solution()
print(s.convert(1921))  # Should print One Hundred Twenty Three
