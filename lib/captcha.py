DATA_FILE = './captcha_log.json'

GUMP_ID = 0x46df63e6
QUESTIONS = {
    'What is the first letter in the word "Ultima"?': 'u',
    'What game are you playing?': 'Ultima',
    'How many banks are in Britain?': '2',
}

class GumpData:
    def __init__(self, layout, text):
        self.layout = layout
        self.text = text

    def _clean_text(self, text):
        text = text.replace('<BASEFONT COLOR=#FFFFFF>', '')
        text = text.replace('<CENTER>', '')
        text = text.replace('</CENTER>', '')
        text = text.replace('</BASEFONT>', '')
        return text

    def get_question(self):
        if self.text:
            return self._clean_text(self.text[3])
        return None

    def get_answers(self):
        if self.text:
            return [ self._clean_text(s) for s in self.text[4:]]
        return None

    def get_buttons(self):
        buttons = []
        answers = self.get_answers()
        if self.layout:
            for b in self.layout.split('}{'):
                if 'button' in b:
                    buttons.append(b.strip().split(' ')[-1])
        return dict(zip(answers, buttons))

    def solve(self):
        buttons = self.get_buttons()
        question = self.get_question()
        if question in QUESTIONS:
            answer = QUESTIONS[question]
            if answer in buttons:
                return buttons[answer]
        else:
            self.save_data()

        # TODO: save question and answers to file
        return None

    def save_data(self):
        with open(DATA_FILE, 'a') as f:
            text = "{question};{answers}\n".format(question=self.get_question(), answers=self.get_answers())
            f.write(text)


class CaptchaResolver:

    def start(self):
        while True:
            if Gumps.HasGump(GUMP_ID):
                gd = Gumps.GetGumpData(GUMP_ID)
                gd = GumpData(gd.gumpLayout, gd.gumpText)

