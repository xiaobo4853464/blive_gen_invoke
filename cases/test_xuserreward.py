"""
Auto gen. Do not change.
Any question please connect @好人索尔
"""

from src.xuserreward import Xuserreward


class TestXuserreward(object):
    @classmethod
    def setup_class(cls):
        cls.mygrpc = Xuserreward()

    def test_achievement_add(self):
        r = self.mygrpc.achievement_add()
        print(r)

    def test_achievement_receive(self):
        r = self.mygrpc.achievement_receive()
        print(r)

    def test_add(self):
        r = self.mygrpc.add(name=1,duration=1,img_url=1,operator=1)
        print(r)

    def test_add_score(self):
        r = self.mygrpc.add_score()
        print(r)

    def test_app_get_sign_info(self):
        r = self.mygrpc.app_get_sign_info()
        print(r)

    def test_cancel_title(self):
        r = self.mygrpc.cancel_title()
        print(r)

    def test_card_add(self):
        r = self.mygrpc.card_add(name=1,icon_id=1,url=1,style=1,type=1,img=1)
        print(r)

    def test_card_check(self):
        r = self.mygrpc.card_check(name=1)
        print(r)

    def test_card_enable(self):
        r = self.mygrpc.card_enable(id=1)
        print(r)

    def test_card_list(self):
        r = self.mygrpc.card_list(pn=1,ps=1)
        print(r)

    def test_clear_light_title(self):
        r = self.mygrpc.clear_light_title()
        print(r)

    def test_clear_user_cache(self):
        r = self.mygrpc.clear_user_cache(uid=1)
        print(r)

    def test_del_(self):
        r = self.mygrpc.del_(uid=1)
        print(r)

    def test_del_master(self):
        r = self.mygrpc.del_master()
        print(r)

    def test_del_sub(self):
        r = self.mygrpc.del_sub()
        print(r)

    def test_delete_anchor_emoticon(self):
        r = self.mygrpc.delete_anchor_emoticon()
        print(r)

    def test_delete_effect(self):
        r = self.mygrpc.delete_effect(id=1)
        print(r)

    def test_do_sign(self):
        r = self.mygrpc.do_sign()
        print(r)

    def test_edit(self):
        r = self.mygrpc.edit(img_url=1,id=1,operator=1)
        print(r)

    def test_edit_status(self):
        r = self.mygrpc.edit_status()
        print(r)

    def test_effect_detail(self):
        r = self.mygrpc.effect_detail(id=1)
        print(r)

    def test_effect_list(self):
        r = self.mygrpc.effect_list()
        print(r)

    def test_emoticon_operation(self):
        r = self.mygrpc.emoticon_operation(type=1,unique_id=1,opt_id=1,user_id=1,room_id=1)
        print(r)

    def test_get(self):
        r = self.mygrpc.get(id=1)
        print(r)

    def test_get_achievement_list(self):
        r = self.mygrpc.get_achievement_list()
        print(r)

    def test_get_anchor_emoticions_list(self):
        r = self.mygrpc.get_anchor_emoticions_list()
        print(r)

    def test_get_anchor_emoticon_guide_step(self):
        r = self.mygrpc.get_anchor_emoticon_guide_step(uid=1)
        print(r)

    def test_get_by_id(self):
        r = self.mygrpc.get_by_id()
        print(r)

    def test_get_by_tid(self):
        r = self.mygrpc.get_by_tid()
        print(r)

    def test_get_by_uid(self):
        r = self.mygrpc.get_by_uid(uid=1)
        print(r)

    def test_get_emoticon_jurisdiction(self):
        r = self.mygrpc.get_emoticon_jurisdiction()
        print(r)

    def test_get_emoticon_list(self):
        r = self.mygrpc.get_emoticon_list(type=1,page_index=1,page_size=1)
        print(r)

    def test_get_emoticons(self):
        r = self.mygrpc.get_emoticons()
        print(r)

    def test_get_emoticons_new(self):
        r = self.mygrpc.get_emoticons_new()
        print(r)

    def test_get_front_room_icon(self):
        r = self.mygrpc.get_front_room_icon(room_id=1)
        print(r)

    def test_get_glory_visible(self):
        r = self.mygrpc.get_glory_visible(uid=1)
        print(r)

    def test_get_hot_emoticon(self):
        r = self.mygrpc.get_hot_emoticon()
        print(r)

    def test_get_last_month_sign_info(self):
        r = self.mygrpc.get_last_month_sign_info()
        print(r)

    def test_get_list(self):
        r = self.mygrpc.get_list()
        print(r)

    def test_get_reward(self):
        r = self.mygrpc.get_reward()
        print(r)

    def test_get_room_bind(self):
        r = self.mygrpc.get_room_bind(room_id=1)
        print(r)

    def test_get_room_card_list(self):
        r = self.mygrpc.get_room_card_list(room_id=1)
        print(r)

    def test_get_user_card_glory(self):
        r = self.mygrpc.get_user_card_glory(uid=1)
        print(r)

    def test_get_user_card_title(self):
        r = self.mygrpc.get_user_card_title(uid=1)
        print(r)

    def test_get_user_card_title_new(self):
        r = self.mygrpc.get_user_card_title_new(uid=1)
        print(r)

    def test_get_user_glory_all(self):
        r = self.mygrpc.get_user_glory_all(uid=1)
        print(r)

    def test_get_user_glory_list(self):
        r = self.mygrpc.get_user_glory_list(uid=1)
        print(r)

    def test_get_user_light_title(self):
        r = self.mygrpc.get_user_light_title()
        print(r)

    def test_get_user_show_title(self):
        r = self.mygrpc.get_user_show_title()
        print(r)

    def test_get_user_status(self):
        r = self.mygrpc.get_user_status()
        print(r)

    def test_get_user_title_all(self):
        r = self.mygrpc.get_user_title_all()
        print(r)

    def test_get_user_title_list(self):
        r = self.mygrpc.get_user_title_list()
        print(r)

    def test_get_wearing_title(self):
        r = self.mygrpc.get_wearing_title()
        print(r)

    def test_icon_add(self):
        r = self.mygrpc.icon_add(name=1,icon_url=1)
        print(r)

    def test_icon_enable(self):
        r = self.mygrpc.icon_enable(id=1)
        print(r)

    def test_icon_list(self):
        r = self.mygrpc.icon_list()
        print(r)

    def test_insert_anchor_emoticions(self):
        r = self.mygrpc.insert_anchor_emoticions()
        print(r)

    def test_list(self):
        r = self.mygrpc.list(uid=1)
        print(r)

    def test_logs(self):
        r = self.mygrpc.logs(uid=1)
        print(r)

    def test_plug_sign(self):
        r = self.mygrpc.plug_sign(uid=1)
        print(r)

    def test_plug_sign_reward(self):
        r = self.mygrpc.plug_sign_reward(uid=1)
        print(r)

    def test_private_domain_authentication(self):
        r = self.mygrpc.private_domain_authentication(uid=1)
        print(r)

    def test_private_domain_delete_emoticon(self):
        r = self.mygrpc.private_domain_delete_emoticon(uid=1)
        print(r)

    def test_private_domain_emoticon_authentication(self):
        r = self.mygrpc.private_domain_emoticon_authentication(uid=1,target_id=1,emoticon_unique=1)
        print(r)

    def test_private_domain_emoticon_list(self):
        r = self.mygrpc.private_domain_emoticon_list(uid=1,target_id=1)
        print(r)

    def test_private_domain_emoticon_list_by_target_id(self):
        r = self.mygrpc.private_domain_emoticon_list_by_target_id(uid=1)
        print(r)

    def test_private_domain_emoticon_publish(self):
        r = self.mygrpc.private_domain_emoticon_publish(uid=1)
        print(r)

    def test_private_domain_update_emoticon_pkg_info(self):
        r = self.mygrpc.private_domain_update_emoticon_pkg_info(uid=1)
        print(r)

    def test_publish_emoticon(self):
        r = self.mygrpc.publish_emoticon()
        print(r)

    def test_rebuild_list_cache(self):
        r = self.mygrpc.rebuild_list_cache(uid=1)
        print(r)

    def test_remove_effect_cache(self):
        r = self.mygrpc.remove_effect_cache(effect_id=1)
        print(r)

    def test_remove_user_cache(self):
        r = self.mygrpc.remove_user_cache(uid=1)
        print(r)

    def test_room_add(self):
        r = self.mygrpc.room_add(room_id=1,operator=1)
        print(r)

    def test_room_bind(self):
        r = self.mygrpc.room_bind()
        print(r)

    def test_room_del(self):
        r = self.mygrpc.room_del(id=1)
        print(r)

    def test_room_list(self):
        r = self.mygrpc.room_list(pn=1,ps=1)
        print(r)

    def test_save_effect(self):
        r = self.mygrpc.save_effect()
        print(r)

    def test_send(self):
        r = self.mygrpc.send(card_record_id=1,send_uid=1,recv_uid=1)
        print(r)

    def test_send_dm_emoticon_check_auth(self):
        r = self.mygrpc.send_dm_emoticon_check_auth()
        print(r)

    def test_set_anchor_emoticon_guide_step(self):
        r = self.mygrpc.set_anchor_emoticon_guide_step(step=1,uid=1)
        print(r)

    def test_set_effect_status(self):
        r = self.mygrpc.set_effect_status(id=1)
        print(r)

    def test_set_online(self):
        r = self.mygrpc.set_online()
        print(r)

    def test_set_reward(self):
        r = self.mygrpc.set_reward()
        print(r)

    def test_statistic(self):
        r = self.mygrpc.statistic()
        print(r)

    def test_triger_effect(self):
        r = self.mygrpc.triger_effect(uid=1,target_id=1,room_id=1)
        print(r)

    def test_triger_entry(self):
        r = self.mygrpc.triger_entry(uid=1,target_id=1,room_id=1,uname=1,face=1,**from_=1)
        print(r)

    def test_triger_follow(self):
        r = self.mygrpc.triger_follow(uid=1,roomid=1)
        print(r)

    def test_triger_share(self):
        r = self.mygrpc.triger_share(uid=1,roomid=1)
        print(r)

    def test_triger_welcome(self):
        r = self.mygrpc.triger_welcome(uid=1,roomid=1)
        print(r)

    def test_update_pkg_info(self):
        r = self.mygrpc.update_pkg_info(update_type=1,emoticon_id=1)
        print(r)

    def test_use(self):
        r = self.mygrpc.use()
        print(r)

    def test_user_sign_info(self):
        r = self.mygrpc.user_sign_info(uid=1)
        print(r)

    def test_wear_title(self):
        r = self.mygrpc.wear_title()
        print(r)

    def test_web_get_sign_info(self):
        r = self.mygrpc.web_get_sign_info()
        print(r)

