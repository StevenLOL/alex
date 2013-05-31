#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

if __name__ == "__main__":
    import autopath
import __init__

from alex.components.slu.da import DialogueAct
from alex.components.nlg.template import TemplateNLG
from alex.utils.config import Config, as_project_path

CONFIG_DICT = {
    'NLG': {
        'debug': True,
        'type': 'Template',
        'Template' : {
            'model': as_project_path('applications/CamInfoRest/nlgtemplates.cfg')
        },
    }
}

class TestTemplateNLG(unittest.TestCase):
    def test_template_nlg(self):

        cfg = Config(config=CONFIG_DICT)
        nlg = TemplateNLG(cfg)

        da = DialogueAct('affirm()&inform(task="find")&inform(pricerange="cheap")')
        correct_text = u"Ok, you are looking for something in the cheap price range."
        generated_text = nlg.generate(da)

        s = []
        s.append("")
        s.append("Input DA:")
        s.append(unicode(da))
        s.append("")
        s.append("Correct text:")
        s.append(unicode(correct_text))
        s.append("")
        s.append("Generated text:")
        s.append(unicode(generated_text))
        s.append("")
        print '\n'.join(s)

        self.assertEqual(unicode(correct_text), unicode(generated_text))

    def test_template_nlg_r(self):
        cfg = Config(config=CONFIG_DICT)
        nlg = TemplateNLG(cfg)

        da = DialogueAct('affirm()&inform(pricerange="cheap")&inform(task="find")')
        correct_text = "Ok, you are looking for something in the cheap price range."
        generated_text = nlg.generate(da)

        s = []
        s.append("")
        s.append("Input DA:")
        s.append(unicode(da))
        s.append("")
        s.append("Correct text:")
        s.append(unicode(correct_text))
        s.append("")
        s.append("Generated text:")
        s.append(unicode(generated_text))
        s.append("")
        print '\n'.join(s)

        self.assertEqual(unicode(correct_text), unicode(generated_text))

if __name__ == '__main__':
    unittest.main()