class TextDisplay:

    def star_style(self, text):
        return "★ " + text + " ★";

    def wave_style(self, text):
        return "~~ " + text + " ~~";

display = TextDisplay();
print(display.star_style("합격을 축하합니다"))
print(display.wave_style("오늘 점심은 스파게티"))