class WU:
    def __init__(self):
        with open('suratha_wu_replacements_edited.txt', encoding='utf-8') as f:
            lines=f.read().split('\n')
            replacements=[]
            for line in lines:
                if line.count('~')==1:
                    replacements.append(line.split('~'))
                else:
                    pass
                    #print(line)
                    #print('Error!')
            self.replacements=[tuple(r) for r in replacements]
            print(len(replacements),'WU to Unicode replacements read!')
    def to_unicode(self,text):
        for a,b in self.replacements:
            text=b.join(text.split(a))
        return text

    def self_test(self):
        text_wu="""jÄHf¤âš 20M« ü‰wh©oš nk‰bfhŸs¥g£l
        C®¥bga® bjhl®ghd MŒîfS¡F mo¥gilahf
        18M« ü‰wh©oš nkiynja§fËš nk‰bfhŸs¥g£l
        ïl¥bgauhŒî mikªjJ. ï¤Jiwia m¿Éaš
        tÊ¥g£l MŒî¤Jiwahf ts®¤bjL¤jd®. ï¤Jiw
        tuyhW, bkhÊÆaš JiwfËš mirîfis V‰gL¤âaJ.
        mj‹ fhuzkhf ïl¥bgauhŒî cyfsÉš ftd¥
        gL¤j¥g£L, nk‰f©l ïu©L ÃiyfËš cyfsÉY«
        ïªâahÉY« F¿¥ghf¤ jÄHf¤âY« ïl¥bga®
        bjhl®ghd MŒîfŸ nk‰bfhŸs¥g£ld. tŸsyh®
        (1828-1874) C®¥bgauhŒÉš ÉU¥g« fh£odh®
        v‹whY« bgÇjhf <LglÉšiy. 1946ïš btËahd
        uh. ã. nrJ¥ãŸisÆ‹ CU« ngU« v‹D« üš
        go¥gj‰F¢ Ritahf ïU¥ãD« MŒî bjhŒîilajhf
        mikªJŸsJ. (2008:206). âÇáuòu« kfhÉ¤Jth‹
        Ûdh£á Rªju«ãŸis vGâa jy òuhz§fËY«
        C®¥bga® g‰¿a fhuz§fŸ Tw¥g£LŸsd."""

        text_uni="""தமிழகத்தில் 20ஆம் நூற்றாண்டில் மேற்கொள்ளப்பட்ட
        ஊர்ப்பெயர் தொடர்பான ஆய்வுகளுக்கு அடிப்படையாக
        18ஆம் நூற்றாண்டில் மேலைதேயங்களில் மேற்கொள்ளப்பட்ட
        இடப்பெயராய்வு அமைந்தது. இத்துறையை அறிவியல்
        வழிப்பட்ட ஆய்வுத்துறையாக வளர்த்தெடுத்தனர். இத்துறை
        வரலாறு, மொழியியல் துறைகளில் அசைவுகளை ஏற்படுத்தியது.
        அதன் காரணமாக இடப்பெயராய்வு உலகளவில் கவனப்
        படுத்தப்பட்டு, மேற்கண்ட இரண்டு நிலைகளில் உலகளவிலும்
        இந்தியாவிலும் குறிப்பாகத் தமிழகத்திலும் இடப்பெயர்
        தொடர்பான ஆய்வுகள் மேற்கொள்ளப்பட்டன. வள்ளலார்
        (1828-1874) ஊர்ப்பெயராய்வில் விருப்பம் காட்டினார்
        என்றாலும் பெரிதாக ஈடுபடவில்லை. 1946இல் வெளியான
        ரா. பி. சேதுப்பிள்ளையின் ஊரும் பேரும் என்னும் நூல்
        படிப்பதற்குச் சுவையாக இருப்பினும் ஆய்வு தொய்வுடையதாக
        அமைந்துள்ளது. (2008:206). திரிசிரபுரம் மகாவித்துவான்
        மீனாட்சி சுந்தரம்பிள்ளை எழுதிய தல புராணங்களிலும்
        ஊர்ப்பெயர் பற்றிய காரணங்கள் கூறப்பட்டுள்ளன."""

        assert self.to_unicode(text_wu)==text_uni