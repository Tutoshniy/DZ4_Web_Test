import request
import logging


def test_1(login):
    logging.info("Start test 1")
    assert "Жаренные сосиски" not in request.getpost(login)


def test_create_post(login):
    logging.info("Start test 2")
    description = request.create_post(login, 'Табакси', 'Короткое описание расы Табакси', """Родом из странных и 
                                                                                          далёких земель, 
                                                                                          странствующие табакси – 
                                                                                          кошкоподобные гуманоиды, 
                                                                                          которых любопытство 
                                                                                          заставляет собирать 
                                                                                          интересные артефакты, 
                                                                                          записывать рассказы и 
                                                                                          истории, и осматривать все 
                                                                                          чудеса в мире. Отъявленные 
                                                                                          путешественники, 
                                                                                          любознательные табакси 
                                                                                          редко на долго оседают на 
                                                                                          одном месте. Их врожденный 
                                                                                          характер толкает их 
                                                                                          раскрывать тайны и 
                                                                                          находить потерянные 
                                                                                          сокровища и легенды.""")
    assert description in request.get_post_description(login)
