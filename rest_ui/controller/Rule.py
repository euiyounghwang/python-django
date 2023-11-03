

class Rule(object):
    
    def __init__(self):
        self.header = {
            "Content-Type":"application/json",
            # "X-Client-Id":"6786787678f7dd8we77e787",
            # "X-Client-Secret":"96777676767585",
        }
   
        self.payload = {
            "include_basic_aggs": "true",
            "pit_id": "",
            "query_string": "video",
            "ids_filter": ["*"],
            "direction" : "right",
            "size": 10,
            "sort_order": "DESC",
            "start_date": "2021 01-01 00:00:00"
        }
        
        self.response_sample = {
            "message" : {
                "total": {
                    "value": 122,
                    "relation": "eq"
                },
                "max_score": None,
                "hits": [
                    {
                    "_index": "test_omnisearch_v2",
                    "_id": "eN-en4oBRCqtw0GAkM6w",
                    "_score": 7.036625,
                    "_source": {
                        "title": "Sadako 3D",
                        "ethnicity": "Japanese",
                        "director": "Tsutomu Hanabusa",
                        "cast": "Satomi Ishihara, Koji Seto",
                        "genre": "horror",
                        "plot": "A mysterious, white-clad man drops a long-haired woman into a well. The well is full of women, all with long hair, all dressed in night-dresses.\nThirteen years after the original film, two suicides prompt Detective Koiso and his partner to investigate a string of mysterious deaths. The deaths involve video played on devices; just before the deaths, a voice says, \"You're not the one.\" While Koiso is unconvinced, his partner deduces that the deaths are the result of a cursed video that online artist Seiji Kashiwada created.\nAkane Ayukawa, teacher of a schoolgirl who died, discovers the schoolgirl's best friend Risa had been looking into the cursed video. The video had been deleted, but the Error 404 message in its wake prompts the video to play when the viewer is alone. In it, Kashiwada allows himself to be killed by a long-haired woman. When the video ends, Risa is attacked; Akane arrives just in time to save her. The ghost tells Akane that she is \"the one\". Akane screams, and the computer is destroyed. Meanwhile, Koiso and his partner scout Kashiwada's apartment, noting the furniture and decorative wallpaper, which look like a set. The landlady notes that everything is superficial.\nAkane is a telekinetic who displayed her power years ago when a maniac attacked her high school. Though she saved the school, she was branded a freak. Takanori Andō, son of Mitsuo Andō from the previous film, and a boy who appreciates her abilities, grows up to be her boyfriend. She soon realizes the video is targeted at her when, at their home, the video plays and the woman appears. Multiple screens show the woman attacking. Takanori and Akane run to a street, where they believe themselves safe, but a large LCD display truck shows a giant version of the ghost, who snatches Takanori away.\nUntil his partner commits suicide in front of him, Detective Koiso continues to doubt the existence of the film, even when it is revealed that the original broadcast of the online video killed its initial viewers and employees of the site where it was uploaded. Koiso makes his way to Kashiwada's apartment, eager to find answers. He discovers the wallpaper is a horde of white butterflies hiding notes and history. Kashiwada had been attempting to resurrect Sadako Yamamura, as revenge against the human populace for persecuting him. He initially kidnapped long-haired women and threw them down the well, alive. However, when it was revealed that a body could not be found that way, he orchestrated the \"cursed video\" so that the video would find the perfect host for her.\nKoiso finds Akane, whom he'd interrogated previously, and the two of them journey to the old Yamamura household. It no longer has the inn, and a \"new\" decrepit mall was beside the well. However, upon approach to the well, a freakish-looking Sadako facsimile appears and attacks Koiso, biting his neck. The women that had been thrown into the well had become imperfect versions of Sadako. They attack Akane, but with stealth and resistance, Akane prevails against the imperfect Sadakos.\nWhen she arrives at the center of the derelict building, she discovers Takanori had been trapped in a mobile phone at the center of the room. A legion of imperfect Sadakos arrive, but her fear triggers her telekinetic powers, which decimates them. Akane is transported to the roof where the \"real\" Sadako has been waiting. Sadako says they are exactly the same, which Akane denies; Sadako uses her powers to destroy, while she helps people. Seeing Takanori with a knife to his throat, Akane trades herself for his life. Sadako agrees and goes into her. Akane is overlain with an impossible amount of the ghost's hair and is buried inside it.\nTakanori, now free from Sadako's thrall, destroys the phone. The roof gives and Akane drops to the floor below covered in Sadako's hair. However, she escapes alive. In a mid-credits scene, It was shown that just outside the building beside the well, Kashiwada's landlord moves away and her words, \"Isn't it all artificial?\" echo. In the post-credits scene, the intro to Kashiwada's video plays again. However, his introduction changes. \"Here we go again.\"",
                        "year": 2012,
                        "wiki_page": "https://en.wikipedia.org/wiki/Sadako_3D"
                    },
                    "highlight": {
                        "plot": [
                        " involve <b><font color=red>video</font></b> played on devices; just before the deaths, a voice says, \"You're not the one.\" While Koiso is unconvinced, his partner deduces"
                        ]
                    },
                    "sort": [
                        7.036625,
                        "Sadako 3D",
                        4294968157
                    ]
                }
            ]
            }
        }
        
    def get_header(self):
        return self.header
        
    def get_payload(self):
        return self.payload
        
    def get_search_result(self):
        return self.response_sample