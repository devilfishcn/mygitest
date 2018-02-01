#!/usr/bin/env python
# -*- coding: utf-8 -*-

import channel
import handlers
import channel.activity
import channel.code
import channel.ctrip
import channel.cheyouhui
import channel.daikuanwang
import channel.intelligence
import channel.interface
import channel.resend
import channel.interface_higher
import channel.interface_ticket
import channel.jd
import channel.oppo
import channel.oupeng
import channel.survey
import channel.survey_edm
import channel.survey_email
import channel.tongcheng
import channel.tongcheng_travel
import channel.tongcheng_edm
import channel.weipiao
import channel.didi
import channel.pingan
import channel.egou
import channel.pingan_vaccines
import channel.dlb_page
import channel.user_recall
import channel.linktech
import channel.appointment
import channel.ruishi
import handlers.detail_tkfz
import handlers.mail_stat
import channel.uber
import channel.daduhui
import channel.phone_captcha
import channel.uc
import channel.kaola
import channel.taikang
import channel.qq
import channel.calculate_premium
import channel.channel_no_idno
import channel.duiba
import channel.tv_yaoyiyao
import channel.jrtt
import channel.xiche
import channel.e_bank
import channel.clothes
import image_captcha
import channel.shanming
import channel.weiche
import channel.car_home
import channel.ele
import channel.zonghe
import channel.xcar
import channel.duomi
import channel.shenma
import channel.sougou
import channel.child
import channel.calculate_zhijie
import channel.mobile2city
import channel.gooyo
import channel.meipian
import channel.mogubao
import channel.huafei
import channel.tweixin
import channel.activities_handler
import channel.tuia
import channel.kuhua
import channel.forward
import channel.pinzhong
import channel.pingan_wifi
import channel.youzhong
import channel.insurance_msg
import channel.bianxianmao
import channel.kuaiduibao
import channel.iqiyi
import channel.quanmama
import channel.qianfang
import channel.guahao114
import channel.zhongbaojinfu
import channel.calculate_taikang
import channel.redirect
import channel.pa_tk_double
import channel.lottery
import channel.qianguanzi
import channel.bainian
import channel.cash_card
import channel.daikuan
import channel.daikuan3
import channel.langge
import channel.xyqianbao
import channel.chediandian
import channel.interface_rongyitui
import channel.cixuanfu
import insurance.handlers.insurance_remind
import insurance.callback.chuanglan
import insurance.handlers.page_handler
import insurance.channel.interface_duiba
import insurance.out_api.bjlt.views
import insurance.out_api.quner.views
import insurance.out_api.market_stat.views
import insurance.out_api.market_stat.current
import insurance.out_api.partner_stat.views
import insurance.out_api.partner_stat.current
import insurance.out_api.baixing.views
import insurance.out_api.real_time_stat.views
import insurance.local_api.policy_checker.views
import insurance.local_api.pingan_policy_parser.views
import insurance.local_api.show_captcha.views
import insurance.lottery.egg
import insurance.lottery.wabao
import insurance.lottery.carnival
import insurance.lottery.guaquan
import insurance.lottery.chailiwu
import insurance.lottery.pick
import insurance.lottery.red_packet
import weixin.wxhandler
import weixin.loan.loan_handlers
import weixin.insurance_wx
import shop.jingpin_shop
import page_base
import channel.youhaoya






HANDLERS= [
    # 邮件投诉相关
    (r"/complain", handlers.mail_stat.HandlerComplain),
    (r"/unsubscribe", handlers.mail_stat.HandlerUnsubscribe),

    (r"/submit", channel.interface.InterfaceHandler),
    (r"/commit", channel.interface.InterfaceHandler),
    # (r"/eva", channel.interface.InterfaceHandler),
    (r"/ctrip", channel.ctrip.InterfaceHandlerCtrip),
    (r"/zhixing", channel.ctrip.InterfaceHandlerCtrip),
    # (r"/gtgj", channel.interface_ticket.InterfaceHandlerQunartrain),
    (r"/qunar", channel.interface_ticket.InterfaceHandlerQunartrain),
    (r"/qunartrain", channel.interface_ticket.InterfaceHandlerQunartrain),
    (r"/114piao", channel.interface_ticket.InterfaceHandlerQunartrain),
    (r"/insurance/ticket", channel.interface_ticket.InterfaceHandlerQunartrain),
    (r"/insurance/enhanced", channel.interface_ticket.InterfaceEnhancedHandler),
    (r"/tk_insurance/enhanced", channel.interface_ticket.InterfaceTaikangEnhancedHandler),
    (r"/insurance/rongyitui", channel.interface_rongyitui.InterfaceHandlerRongYiTui),
    (r"/activity/sdpa2", channel.interface_ticket.InterfaceHandlerShenDeng),
    (r"/activity/sdpa3", channel.interface_ticket.InterfaceHandlerShenDeng3),
    (r"/activity/sdpa4", channel.interface_ticket.InterfaceHandlerShenDeng4),
    (r"/activity/sdpa5", channel.interface_ticket.InterfaceHandlerShenDeng5),
    (r"/activity/sdpa6", channel.interface_ticket.InterfaceHandlerShenDeng6),
    (r"/activity/sdpa7", channel.interface_ticket.InterfaceHandlerShenDeng7),
    (r"/activity/sdpa8", channel.interface_ticket.InterfaceHandlerShenDeng8),
    (r"/activity/daiba1", channel.interface_ticket.InterfaceHandlerDaiBa),
    (r"/activity/weicheapi", channel.interface_ticket.InterfaceHandlerWeiChe),
    (r"/insurance/cjyzapi", channel.interface_ticket.InterfaceHandlerChaoJiYuanZhuo),
    # 无身份证的对外接口
    (r"/interface/noid", channel.interface_ticket.InterfaceHandlerNoId),
    # 黑牛平安对外接口
    (r"/interface/heiniupa", channel.interface_ticket.InterfaceHeiniuPingAnHandler),
    (r"/insurance/resend", channel.resend.InterfaceHandler2),
    #(r"/insurance/resend/38lmfpkF8D13zb", channel.resend.ManuallySend),
    (r"/insurance/resend/lmd8pkF138dfmb", channel.resend.ManullySendSingle),
    (r"/mogubao/data", channel.mogubao.MoGuBaoData),

    # (r"/yysk", channel.InterfaceHandlerYysk),
    # (r"/ppcar", channel.interface_higher.InterfaceHandlerHigh),
    (r"/ywsmart", channel.interface_higher.InterfaceHandlerHigh),
    # (r"/youyuan", channel.interface_higher.InterfaceHandlerHigh),
    (r"/dtbsmart", channel.interface_higher.InterfaceHandlerHigh),

    # (r"/trip", channel.activity.PageHandler),
    # (r"/mtrip", channel.activity.MobilePageHandler),
    # (r"/oppo", channel.oppo.PageHandlerOppo),
    (r"/weipiao", channel.weipiao.MobilePageHandlerWeipiao),
    (r"/FreeInsurancePC", channel.tongcheng.TongchengPageHandler),
    (r"/FreeInsuranceWap", channel.tongcheng.MobileTongchengPageHandler),
    (r"/questionnaire1", channel.tongcheng.TongchengQuestionnaireHandler),
    (r"/mquestionnaire1", channel.tongcheng.MobileTongchengQuestionnaireHandler),
    (r"/questionnaire_ywdd", channel.tongcheng.DiDiQuestionnaireHandler),
    (r"/questionnaire_ywuber", channel.tongcheng.UberQuestionnaireHandler),
    (r"/questionnaire_sdkaola", channel.tongcheng.KaolaQuestionnaireHandler),
    (r"/questionnaire_didi", channel.tongcheng.DiDiQuestionnaireHandler),
    (r"/questionnaire_didi_new", channel.tongcheng.NewDiDiQuestionnaireHandler),
    (r"/questionnaire_ele", channel.tongcheng.EleQuestionnaireHandler),
    (r"/questionnaire_xiche", channel.tongcheng.XiCheQuestionnaireHandler),
    (r"/questionnaire_huafei", channel.tongcheng.HuaFeiQuestionnaireHandler),
    (r"/questionnaire_choujiang", channel.tongcheng.ChouJiangQuestionnaireHandler),
    (r"/questionnaire_weiche", channel.tongcheng.WeiCheQuestionnaireHandler),
    (r"/questionnaire_iqiyi", channel.tongcheng.IQiYiQuestionnaireHandler),
    (r"/questionnaire_tongcheng", channel.tongcheng.TongChengTravelQuestionnaireHandler),
    (r"/questionnaire_liuliang", channel.tongcheng.LiuLiangQuestionnaireHandler),
    (r"/questionnaire_liuliang_189_wx", channel.tongcheng.Weixin189LiuLiangQuestionnaireHandler),
    (r"/insurance_explain", channel.tongcheng.InsuranceExplainHandler),
    (r"/questionnaire_jinbi", channel.tongcheng.JinBiQuestionnaireHandler),
    (r"/questionnaire_jingdong", channel.tongcheng.JingDongQuestionnaireHandler),
    (r"/questionnaire_chediandian", channel.chediandian.CheDianDianQuestionnaireHandler),
    (r"/questionnaire_pawifiliuliang", channel.tongcheng.PaWifiLiuLiangQuestionnaireHandler),
    (r"/questionnaire_ofo", channel.tongcheng.PAWifiOfoQuestionnaireHandler),
    (r"/questionnaire_mobai", channel.tongcheng.HeiNiuMoBaiQuestionnaireHandler),
    (r"/questionnaire_jinbi4", channel.tongcheng.JinBi4QuestionnaireHandler),
    (r"/questionnaire_caipiao1", channel.tongcheng.CaiPiaoQuestionnaireHandler),
    (r"/questionnaire_mgb_caipiao1", channel.tongcheng.MGBCaiPiaoQuestionnaireHandler),
    (r"/questionnaire_didi_new_mgb", channel.tongcheng.NewDiDiQuestionnaireHandler_MGB),
    (r"/questionnaire_qianguanzi", channel.tongcheng.QianGuanZiQuestionnaireHandler),
    (r"/questionnaire_qianguanzi_mgb", channel.tongcheng.QianGuanZiQuestionnaireHandler_MGB),
    (r"/questionnaire_meituan", channel.tongcheng.MeiTuanQuestionnaireHandler),
    (r"/questionnaire_meituan2", channel.tongcheng.MeiTuan2QuestionnaireHandler),
    (r"/questionnaire_xinyongka", channel.tongcheng.XinYongKaHuanKuanJinQuestionnaireHandler),
    (r"/questionnaire_xinyongka2", channel.tongcheng.XinYongKaHuanKuanJin2QuestionnaireHandler),


    (r"/FreeInsurance", channel.tongcheng.IndexTongchengPageHandler),
    (r"/activity/tongcheng_maiwaidi", channel.tongcheng.MobileMwdPageHandler),

    # 火车票wifi
    (r"/activity/train_ticket", channel.tongcheng.TrainTicketWifiPageHandler),

    (r"/FreeInsuranceCodePC", channel.code.FreeInsuranceCodePageHandler),
    (r"/FreeInsuranceCodeWap", channel.code.MobileFreeInsuranceCodePageHandler),
    (r"/FreeInsuranceCode", channel.code.IndexCodePageHandler),

    (r"/FreeInsurance2PC", channel.tongcheng_edm.FreeInsurance2PageHandler),
    (r"/FreeInsurance2Wap", channel.tongcheng_edm.MobileFreeInsurance2PageHandler),
    (r"/FreeInsurance2", channel.tongcheng_edm.IndexFreeInsurance2PageHandler),

    (r"/FreeInsurance3PC", channel.survey.FreeInsurance3PageHandler),
    (r"/FreeInsurance3Wap", channel.survey.MobileFreeInsurance3PageHandler),
    (r"/FreeInsurance3", channel.survey.IndexFreeInsurance3PageHandler),

    (r"/FreeInsurance4", channel.survey_email.FreeInsurance4PageHandler),

    (r"/FreeInsurance5PC", channel.survey_edm.FreeInsurance5PageHandler),
    (r"/FreeInsurance5Wap", channel.survey_edm.MobileFreeInsurance5PageHandler),
    (r"/FreeInsurance5", channel.survey_edm.IndexFreeInsurance5PageHandler),
    (r"/jd", channel.jd.IndexJdPageHandler),

    (r"/query/egou", channel.egou.EgouCallbackHandler),
    (r"/activity/egou", channel.egou.EgouPageHandler),
    (r"/activity/didi_nodify", channel.didi.NotificationDidi),
    (r"/activity/didi_wpszj", channel.didi.SubstituteWPSPageHandler),
    (r"/activity/didi_58zj", channel.didi.Substitute58ZiJiaPageHandler),
    (r"/activity/didi_58wz", channel.didi.Substitute58WeiZhangPageHandler),
    (r"/activity/ggxcdd", channel.didi.SubstituteGGXCPageHandler),


    (r"/activity/substitute", channel.didi.SubstituteDidiPageHandler),
    (r"/activity/substitute_wx", channel.didi.SubstituteWeixinDidiPageHandler),
    (r"/activity/substitute_wifi", channel.didi.SubstituteWifiPageHandler),

    (r"/activity/didigift_qm", channel.didi.SurveyQmPageHandler),
    (r"/activity/didigift_zy", channel.didi.SurveyZhongYanPageHandler),
    (r"/activity/didigift_tywx", channel.didi.SurveyTianYiPageHandler),
    (r"/activity/substitute_pd", channel.didi.SubstitutePaiduiPageHandler),
    (r"/activity/didigift_wxpay", channel.didi.SurveyWxPayPageHandler),
    (r"/activity/didigift_wifi", channel.didi.SurveyWifiPageHandler),
    (r"/activity/didigift_youku", channel.didi.SurveyYouKuPageHandler),
    (r"/activity/didigift_shengyang", channel.didi.SurveyShengYangPageHandler),
    (r"/activity/didigift_wifisdk", channel.didi.SurveyWifiSdkPageHandler),
    (r"/activity/didigift_wpsdd", channel.didi.SurveyWPSDDPageHandler),
    (r"/activity/didigift", channel.didi.SurveyDidiPageHandler),
    (r"/activity/didigift2", channel.didi.SurveyDidiPageHandler2),
    (r"/activity/didigift3", channel.didi.SurveyDidiPageHandler3),
    (r"/activity/didipackage", channel.didi.SurveyDidiPackagePageHandler),
    (r"/activity/luolabao_sport", channel.didi.DuoLaBaoSport),
    (r"/activity/luolabao_traffic", channel.didi.DuoLaBaoTrafficAccident),
    (r"/activity/syzj", channel.didi.SubstituteShanYinPageHandler),
    (r"/activity/dsyczj1", channel.didi.DaShenYangCheDidiPageHandler),
    (r"/activity/tnrzj1", channel.didi.TingNaDidiPageHandler),
    (r"/activity/czwyzj1", channel.didi.CheZhuWuYouDidiPageHandler),
    (r"/activity/cddzj1", channel.didi.CheDianDianPageHandler),
    (r"/activity/ykzj1", channel.didi.YingKeDidiPageHandler),
    (r"/activity/wxlkzj1", channel.didi.WeiXinLKDidiPageHandler),
    (r"/activity/zhtzj1", channel.didi.ZhiHuiTuiDidiPageHandler),
    (r"/activity/gzesczj1", channel.didi.GuaZiCarDidiPageHandler),


    # 人人推
    (r"/activity/didi_renrentui", channel.didi.RenRenTuiPageHandler),

    # 微信大号
    (r"/activity/didi_wxdd", channel.didi.WeiXinDHPageHandler),

    # 电视摇一摇
    (r"/activity/tv_guizhou", channel.tv_yaoyiyao.TVGuizhouPageHandler),
    (r"/activity/tv_jilin", channel.tv_yaoyiyao.TVYaoYiYaoJilinPageHandler),
    (r"/activity/tv_chongqing", channel.tv_yaoyiyao.TVChongQinPageHandler),
    (r"/activity/tv_hunan", channel.tv_yaoyiyao.SurveyTVhnPageHandler),
    (r"/activity/tv_dongnan", channel.tv_yaoyiyao.SurveyTVdnPageHandler),
    (r"/activity/tvcdd", channel.tv_yaoyiyao.SurveyTVhdPageHandler),
    (r"/activity/tvzh1", channel.tv_yaoyiyao.TVZongHePageHandler),
    (r"/activity/tvzh2", channel.tv_yaoyiyao.TVZongHe2PageHandler),
    (r"/activity/tvzh3", channel.tv_yaoyiyao.TVZongHe3PageHandler),
    (r"/activity/tvzh4", channel.tv_yaoyiyao.TVZongHe4PageHandler),
    (r"/activity/tvzh5", channel.tv_yaoyiyao.TVZongHe5PageHandler),
    (r"/activity/tvzh6", channel.tv_yaoyiyao.TVZongHe6PageHandler),
    (r"/activity/tvzh7", channel.tv_yaoyiyao.TVZongHe7PageHandler),
    (r"/activity/tvzh8", channel.tv_yaoyiyao.TVZongHe8PageHandler),
    (r"/activity/tvsxk1", channel.tv_yaoyiyao.TVShuxinka),
    (r"/activity/tvsxk2", channel.tv_yaoyiyao.TVShuxinka2),
    (r"/activity/tvsxk3", channel.tv_yaoyiyao.TVShuxinka3),
    (r"/activity/tvsxk4", channel.tv_yaoyiyao.TVShuxinka4),
    (r"/activity/tvsxk5", channel.tv_yaoyiyao.TVShuxinka5),
    (r"/activity/tvsxk6", channel.tv_yaoyiyao.TVShuxinka6),
    (r"/activity/tv_cx", channel.tv_yaoyiyao.TVSelectHandler),
    (r"/activity/tvpingan1", channel.tv_yaoyiyao.TVPinganPageHandler),
    (r"/activity/tv_cetv1", channel.tv_yaoyiyao.TVEducationPageHandler),
    (r"/activity/tv_cetv2", channel.tv_yaoyiyao.TVEducation2PageHandler),
    (r"/activity/tv_cetv3", channel.tv_yaoyiyao.TVEducation3PageHandler),
    (r"/activity/tvdd1", channel.tv_yaoyiyao.TVDiDiPageHandler),
    (r"/activity/tvhf1", channel.tv_yaoyiyao.TVHuaFeiPageHandler),
    (r"/activity/tvzh9", channel.tv_yaoyiyao.TVZongHe9PageHandler),
    (r"/activity/tv_gzzh1", channel.tv_yaoyiyao.TVGuiZhouZongHePageHandler),
    (r"/activity/tv_jlzh1", channel.tv_yaoyiyao.TVJiLinZongHePageHandler),
    (r"/activity/tv_cqzh1", channel.tv_yaoyiyao.TVChongQingZongHePageHandler),
    (r"/activity/tvebank1", channel.tv_yaoyiyao.TVEBankPageHandler),
    (r"/activity/tv_cqcw", channel.tv_yaoyiyao.TVChongQinChunWanPageHandler),
    (r"/activity/tv_cqaqy1", channel.tv_yaoyiyao.ChongQingIQiYiPageHandler),
    (r"/activity/tv_gzaqy1", channel.tv_yaoyiyao.GuiZhouIQiYiPageHandler),
    (r"/activity/tv_hljdd", channel.tv_yaoyiyao.TVHeiLongJiangPageHandler),
    (r"/activity/rytzh1", channel.tv_yaoyiyao.RongYiTuiZongHe1PageHandler),
    (r"/activity/rytzh2", channel.tv_yaoyiyao.RongYiTuiZongHe2PageHandler),
    (r"/activity/tv_gzdk1", channel.tv_yaoyiyao.TVGuiZhouDk1PageHandler),
    (r"/activity/tv_jldk1", channel.tv_yaoyiyao.TVJiLinDK1PageHandler),
    (r"/activity/tv_cqdk1", channel.tv_yaoyiyao.TVChongQingDK1PageHandler),
    (r"/activity/tv_hljdk1", channel.tv_yaoyiyao.TVHeiLongJiangDK1PageHandler),
    (r"/activity/rytzh3", channel.tv_yaoyiyao.RongYiTuiZongHe3PageHandler),
    # 天创
    (r"/activity/(tianchuang[12]0)", channel.tv_yaoyiyao.TianChuangZongHe1PageHandler),
    (r"/activity/(tianchuang[1]?[1-9])", channel.tv_yaoyiyao.TianChuangZongHe1PageHandler),
    (r"/activity/(tianchuang2[1-5])", channel.tv_yaoyiyao.TianChuangZongHe1PageHandler),
    # 电信
    (r"/activity/dianxin1", channel.tv_yaoyiyao.DianXinPageHandler),
    # 随时贷
    (r"/activity/shd1", channel.tv_yaoyiyao.SuiShiDaiPageHandler),
    # 思齐
    (r"/activity/siqi1", channel.tv_yaoyiyao.SiQiPageHandler),
    # 快看
    (r"/activity/kuaikan1", channel.tv_yaoyiyao.KuaiKanPageHandler),
    # 聚合
    (r"/activity/juhe1", channel.tv_yaoyiyao.JuHePageHandler),
    # 非常云
    (r"/activity/feichangyun1", channel.tv_yaoyiyao.FeiChangYun1PageHandler),
    # 品效
    (r"/activity/pinxiao1", channel.tv_yaoyiyao.PinXiao1PageHandler),
    (r"/activity/(pinxiao[2-4])", channel.tv_yaoyiyao.PinXiao2PageHandler),
    (r"/activity/pinxiao5", channel.tv_yaoyiyao.PinXiao5PageHandler),
    # 平安测保
    (r"/calculate_premium/pingan", channel.calculate_premium.CalculatePremium),
    (r"/calculate_premium_mgb/pingan", channel.calculate_premium.CalculatePremium_MGB),
    (r"/calculate_premium/189mail", channel.calculate_premium.Calculate189Mail),

    # 直接投放测保部分
    (r"/activity/tvpacb1", channel.calculate_zhijie.TVPACalculatePremium),
    (r"/calculate_premium/jrttpacb", channel.calculate_zhijie.CalculatePremiumTodayNews),
    (r"/calculate_premium/jrttpacb1", channel.calculate_zhijie.CalculatePremiumTodayNews1),
    (r"/calculate_premium/jrttpacb2", channel.calculate_zhijie.CalculatePremiumTodayNews2),
    (r"/calculate_premium/newcb", channel.calculate_zhijie.CalculatePremiumNewCB),
    (r"/activity/sougoucb1", channel.calculate_zhijie.SouGouCalculatePremium),
    (r"/calculate_premium/sdpacb", channel.calculate_zhijie.CalculatePremiumShenDeng),
    (r"/calculate_premium/yedmcb", channel.calculate_zhijie.CalculatePremiumYWnew),
    (r"/activity/shenmacb1", channel.calculate_zhijie.ShenMaCalculatePremium),
    (r"/activity/tvcb1", channel.calculate_zhijie.TVCalculatePremium),
    (r"/activity/pzjrttpacb1", channel.calculate_zhijie.PZCalculatePremium),
    (r"/activity/pzjrttpacb2", channel.calculate_zhijie.PZCalculatePremium2),
    (r"/activity/pzjrttpacb3", channel.calculate_zhijie.PZCalculatePremium3),
    (r"/activity/pzjrttpacb4", channel.calculate_zhijie.PZCalculatePremium4),
    (r"/activity/pzbdyspacb1", channel.calculate_zhijie.PZBDCalculatePremium1),
    (r"/activity/pzbdyspacb2", channel.calculate_zhijie.PZBDCalculatePremium2),
    (r"/activity/pzbdyspacb3", channel.calculate_zhijie.PZBDCalculatePremium3),
    (r"/activity/pzbdyspacb4", channel.calculate_zhijie.PZBDCalculatePremium4),
    (r"/activity/mjtqcb1", channel.calculate_zhijie.MJTQCalculatePremium1),
    (r"/activity/pzbdsspacb1", channel.calculate_zhijie.PZBDSSCalculatePremium),


    #快用
    (r"/activity/kydd", channel.didi.SurveyKuaiYongPageHandler),
    (r"/activity/vaccines", channel.pingan_vaccines.SurveyPinganPageHandler),

    (r"/activity/wjxym1", channel.pingan_vaccines.WenJuanXingPageHandler),

    # 新增品众链接
    (r"/activity/mwd_pzzx", channel.tongcheng.MobilePinZhongMWD),
    (r"/activity/tc_pzzx", channel.tongcheng.MobilePinZhongTC),
    (r"/activity/pinganzj_pzzx", channel.pinzhong.PingAnPinZhongPageHandler),
    (r"/activity/vaccines_pzzx", channel.pingan_vaccines.SurveyPinganPinZhongPageHandler),
    (r"/activity/paidui_pzzx", channel.pinzhong.PaiduiPinZhongPageHandler),
    (r"/activity/pingandc_pzzx", channel.pinzhong.PinZhongPAPageHandler),
    (r"/activity/didi_pzzx", channel.pinzhong.SurveyDidiPingZhong),
    (r"/activity/pzjrttpa1", channel.pinzhong.PinZhongJRTT1PageHandler),
    (r"/activity/pzjrttpa2", channel.pinzhong.PinZhongJRTT2PageHandler),
    (r"/activity/pzjrttpa3", channel.pinzhong.PinZhongJRTT3PageHandler),
    (r"/activity/pzjrttpa4", channel.pinzhong.PinZhongJRTT4PageHandler),
    (r"/activity/pzjrttpazh1", channel.pinzhong.PinZhong1PageHandler),
    (r"/activity/pzjrttpazh2", channel.pinzhong.PinZhong2PageHandler),
    (r"/activity/pzjrttpazh3", channel.pinzhong.PinZhong3PageHandler),
    (r"/activity/pzjrttpazh4", channel.pinzhong.PinZhong4PageHandler),
    (r"/activity/pzbdyszh1", channel.pinzhong.PinZhongBDZH1PageHandler),
    (r"/activity/pzbdyszh2", channel.pinzhong.PinZhongBDZH2PageHandler),
    (r"/activity/pzbdyszh3", channel.pinzhong.PinZhongBDZH3PageHandler),
    (r"/activity/pzbdyszh4", channel.pinzhong.PinZhongBDZH4PageHandler),
    (r"/activity/pzbdyspa1", channel.pinzhong.PinZhongBDPA1PageHandler),
    (r"/activity/pzbdyspa2", channel.pinzhong.PinZhongBDPA2PageHandler),
    (r"/activity/pzbdyspa3", channel.pinzhong.PinZhongBDPA3PageHandler),
    (r"/activity/pzbdyspa4", channel.pinzhong.PinZhongBDPA4PageHandler),
    (r"/activity/pzjrttzj1", channel.pinzhong.PinZhongZiJia1PageHandler),
    (r"/activity/pzjrttzj2", channel.pinzhong.PinZhongZiJia2PageHandler),
    (r"/activity/pzbdsspa1", channel.pinzhong.PinZhongBDSSPA1PageHandler),
    (r"/activity/pzbdsszh1", channel.pinzhong.PinZhongBDSSZH1PageHandler),



    # 哆啦宝
    (r"/activity/duolabao", channel.dlb_page.DuoLaBaoStaticPageHandler),
    (r"/activity/didi_dlbsmart", channel.dlb_page.DuolaBaoSmart),
    (r"/activity/dlbfcb", channel.dlb_page.DuoLaBaoPageHander),
    (r"/activity/vaccines_dlb", channel.dlb_page.SurveyPinganDuoLaBaoPageHandler),
    (r"/activity/yedsym", channel.dlb_page.YuErDaShiPageHandler),
    (r"/activity/dlbdd2", channel.dlb_page.SurveyDuoLaBaoPageHandler2),
    (r"/activity/dlbebank", channel.dlb_page.SurveyDuoLaBaoEBankPageHandler),
    (r"/activity/dlbddcpc1", channel.duiba.DuoLaBaoDiDiCPCPageHandler),
    (r"/activity/dlbmtcpc1", channel.didi.DuoLaBaoMeiTuanPageHandler),

    # 用户召回
    (r"/recall", channel.user_recall.UserRecallPageHandler),
    ("/activity/recall_fcb", channel.taikang.OwnerPageHande),

    # 领克特
    # (r"/promotion/linktech", channel.linktech.LinktechInterface),
    # (r"/activity/linktech", channel.linktech.LinktechPageHandler),
    # (r"/query/linktech", channel.linktech.LinktechCallbackHandler),
    # (r"/activity/linktechdd2", channel.linktech.LinktechDidiPageHandler),
    # (r"/activity/lktpingan", channel.linktech.LinktechPingAnPageHandler),

    # uc
    (r"/activity/didigift_uc", channel.uc.SurveyUcPageHandler),
    (r"/activity/uc123dd3", channel.uc.SurveyUcPageHandler3),
    (r"/activity/uc123pady", channel.uc.SurveyUcPingAnPageHandler),
    (r"/activity/uc123smart", channel.uc.SurveyUcSmartPageHandler),
    (r"/activity/uc123fcb", channel.uc.SurveyUcFeiChangBaoPageHandler),
    (r"/activity/didi_getui", channel.uc.GeTuiPageHandler),
    (r"/activity/ucunion", channel.uc.UnionPageHandler),
    (r"/activity/uc123zj", channel.uc.SurveyUCZiJiaPageHandler),
    (r"/activity/uc123kaola", channel.uc.SurveyUCKaoLaPageHandler),

    # 流量宝
    # (r"/activity/llbdd", channel.didi.SurveyDidiLiuLiangBao),
    # (r"/activity/liuliangbao1", channel.daikuan.LiuLiangBaoPageHandler),
    (r"/activity/liuliangbao1", channel.tv_yaoyiyao.LiuLiangBao1PageHandler),

    # 钱方好近
    (r"/activity/qfhjdd", channel.didi.SurveyDidiQianFangHaoJin),
    (r"/activity/yysdd", channel.didi.SurveyDidiYunYingShang),
    (r"/activity/wnldd", channel.didi.SurveyDidiWanNianLi),
    (r"/activity/sjgjdd", channel.didi.SurveyDidiPhoneManager),
    (r"/activity/xntsdd", channel.didi.SurveyDidiBirdPush),
    (r"/activity/smzdm", channel.didi.SurveyDidiWorthToBuy),
    (r"/activity/ggndd", channel.didi.SurveyDidiGuGuBird),
    (r"/activity/ggndd2", channel.didi.SurveyDidiGuGuBird2),
    (r"/activity/ggndd3", channel.didi.SurveyDidiGuGuBird3),
    (r"/activity/wodd1", channel.didi.SurveyDidiYouSiBanner),
    (r"/activity/zf1dd", channel.didi.SurveyDidiPay),
    (r"/activity/jscydd", channel.didi.SurveyDidiJinShiChuangYu),
    (r"/activity/dmmdd", channel.didi.SurveyDidiDaiMengMao),
    (r"/activity/tvqydd", channel.didi.SurveyDidiQuYaoTV),
    (r"/activity/txgtdd", channel.didi.SurveyDidiTieXiTrain),
    (r"/activity/apdd", channel.didi.SurveyDidiAPPageHandler),
    (r"/activity/ywdd3", channel.didi.SurveyDidiYuWen3PageHandler),
    (r"/activity/tusidd", channel.didi.SurveyDidiTuSiPageHandler),
    (r"/activity/tswxdd1", channel.didi.SurveyDidiTuSi1PageHandler),
    (r"/activity/weipiaodd1", channel.didi.SurveyWeiPiaoPageHandler),
    (r"/activity/58dd1", channel.didi.Survey58DiDiPageHandler),
    (r"/activity/58dd2", channel.didi.Survey58DiDi2PageHandler),
    (r"/activity/hbrldd1", channel.didi.SurveyHongBaoPageHandler),
    (r"/activity/chuanglandd1", channel.didi.SurveyDidiChuangLanPageHandler),
    (r"/activity/tzdwxdd", channel.didi.SurveyDidiTZDWXPageHandler),
    (r"/activity/qmmfdd1", channel.didi.SurveyDidiQMMFPageHandler),
    (r"/activity/jmmdd1", channel.didi.SurveyDidiJMMPageHandler),
    (r"/activity/jmmdd2", channel.quanmama.QuanMaMaDD2PageHandler),
    (r"/activity/jmmdd3", channel.quanmama.QuanMaMaDD3PageHandler),
    (r"/activity/sbqdd1", channel.didi.ShangBuQiDD1PageHandler),
    (r"/activity/sbqdd2", channel.didi.ShangBuQiDD2PageHandler),
    (r"/activity/dsyc1", channel.didi.SurveyDidiDSYC1PageHandler),
    (r"/activity/mmdd1", channel.didi.SurveyDidiMMPageHandler),
    (r"/activity/wnysdd1", channel.didi.SurveyDidiWNYSPageHandler),

    # TKFZ 保险详情页面
    (r"/detail/tkfz", handlers.detail_tkfz.DetailTKFZ),


    # uber
    (r"/activity/ywuber", channel.uber.SurveyUberPageHandler),
    (r"/activity/ywuber2", channel.uber.SurveyUber2PageHandler),


    # 网易考拉
    (r"/activity/sdkaola", channel.kaola.SurveyKoalaPageHandler),


    # 泰康预约投保
    (r"/appointment/taikang", channel.appointment.AppointmentTK),
    (r"/appointment_mgb/taikang", channel.appointment.AppointmentTK_MGB),
    (r"/appointment/sdtkyy", channel.appointment.AppointmentTKShenDeng),
    (r"/appointment/tvtk1", channel.appointment.AppointmentTKTV),
    # 趣头条
    (r"/activity/(qutttk[1-3])", channel.taikang.QuTouTiaoTaiKangPageHander),
    (r"/activity/quttddcpc1", channel.duiba.QuTouTiaoDiDiCPCPageHandler),
    (r"/activity/qttmtcpc1", channel.didi.QuTouTiaoMeiTuanPageHandler),

    # 大众试驾
    (r"/appointment/volkswagen", channel.appointment.AppointmentVolkswagen),
    (r"/appointment/volkswagen_understand", channel.appointment.AppointmentVolkswagenUnderstand),
    (r"/appointment/volkswagen_home", channel.appointment.AppointmentVolkswagenHome),
    (r"/appointment/drivenew", channel.appointment.AppointmentDrive6),
    (r"/appointment/drivenew_understand", channel.appointment.AppointmentDrive6Understand),
    (r"/appointment/drivenew_home", channel.appointment.AppointmentDrive6Home),


    # wps非常保
    (r"/activity/wpsfcb", channel.taikang.WPSPageHander),
    (r"/activity/ywfcb3", channel.taikang.YuWenFCB3PageHander),
    (r"/activity/ywfcb4", channel.taikang.YuWenFCB4PageHander),
    (r"/activity/taikang_ywfcb", channel.taikang.TaikangPageHander),
    (r"/activity/189wxfcb", channel.taikang.TianYiLiuLiangPageHander),
    (r"/activity/jsdx", channel.taikang.JiangSuDianXinPageHander),

    # QQ黄钻会员
    (r"/activity/qqvippasmart", channel.qq.SurveyQQVIPPageHandler),
    (r"/activity/qqvippa1", channel.qq.QQVIPPaPageHandler),
    (r"/activity/qqvipsxk1", channel.qq.QQVIPShuxinkaPageHander),
    (r"/activity/qqvipddh1", channel.qq.QQVIPDaduhuiPageHandler),

    # 平安
    (r"/activity/ddcxpa", channel.pingan.PinganChuXingPageHandler),
    (r"/activity/first", channel.pingan.PinganFirstPageHandler),
    (r"/activity/second", channel.pingan.PinganSecendPageHandler),
    (r"/activity/heiniupady", channel.pingan.PinganHeiNiuPageHandler),
    (r"/activity/jxydtdd", channel.pingan.SurveyJiaXiaoPageHandler),
    (r"/activity/pasfpa1", channel.pingan.PinganSiFangPageHandler),
    (r"/activity/sbqpa1", channel.pingan.ShangBuQi1PageHandler),
    (r"/activity/sbqpa2", channel.pingan.ShangBuQi2PageHandler),
    (r"/activity/wpspawj1", channel.pingan.PinganWPS1PageHandler),


    # 兑吧
    (r"/activity/duibapa", channel.duiba.DuiBaPinganPageHandler),
    (r"/activity/duibapa1", channel.duiba.DuiBaPingan1PageHandler),
    (r"/activity/duibapa2", channel.duiba.DuiBaPingan2PageHandler),
    (r"/activity/duibapa3", channel.duiba.DuiBaPingan3PageHandler),
    (r"/activity/duibapa4", channel.duiba.DuiBaPingan4PageHandler),
    (r"/activity/duibapa5", channel.duiba.DuiBaPingan5PageHandler),
    (r"/activity/duibatk", channel.duiba.DuiBaFeiChangBaoPageHandler),
    (r"/activity/duibatk1", channel.duiba.DuiBaFeiChangBao1PageHandler),
    (r"/activity/duibatk2", channel.duiba.DuiBaFeiChangBao2PageHandler),
    (r"/activity/duibatk3", channel.duiba.DuiBaFeiChangBao3PageHandler),
    (r"/activity/duibatk4", channel.duiba.DuiBaFeiChangBao4PageHandler),
    (r"/activity/duibatk5", channel.duiba.DuiBaFeiChangBao5PageHandler),
    (r"/activity/duibatkcpc1", channel.duiba.DuiBaTaiKangCPCPageHandler),
    (r"/activity/duibauber", channel.duiba.SurveyDuiBaUberPageHandler),
    (r"/activity/vaccines_duiba", channel.duiba.SurveyPinganDuibaPageHandler),
    (r"/activity/substitute_duiba", channel.duiba.SubstituteWifiDuibaPageHandler),
    (r"/activity/tongcheng_dbhksmart", channel.duiba.DuiBaPageHandler),
    (r"/activity/didi_duibadd", channel.duiba.SubstituteDuiBaPageHandler),
    (r"/activity/didi_duibadd2", channel.duiba.SubstituteDuiBaPageHandler2),
    (r"/activity/didi_duibadd3", channel.duiba.SubstituteDuiBaPageHandler3),
    (r"/activity/didi_duibadd4", channel.duiba.SubstituteDuiBaPageHandler4),
    (r"/activity/didi_duibadd5", channel.duiba.SubstituteDuiBaPageHandler5),
    (r"/activity/didi_duibadd6", channel.duiba.SubstituteDuiBaPageHandler6),
    (r"/activity/didi_duibadd7", channel.duiba.SubstituteDuiBaPageHandler7),
    (r"/activity/didi_duibadd8", channel.duiba.SubstituteDuiBaPageHandler8),
    (r"/activity/duibadd_nine", channel.duiba.SubstituteDuiBaPageHandler9),
    (r"/activity/duibadd_ten", channel.duiba.SubstituteDuiBaPageHandler10),
    (r"/activity/duibadd_ele", channel.duiba.SubstituteDuiBaPageHandler11),
    (r"/activity/duibadd_twe", channel.duiba.SubstituteDuiBaPageHandler12),
    (r"/activity/duibadd_thi", channel.duiba.SubstituteDuiBaPageHandler13),
    (r"/activity/duibadd_fou", channel.duiba.SubstituteDuiBaPageHandler14),
    (r"/activity/duibadd_fif", channel.duiba.SubstituteDuiBaPageHandler15),
    (r"/activity/duibaddcpc1", channel.duiba.DuiBaDiDiTestClick1PageHandler),
    (r"/activity/duibaddcpc2", channel.duiba.DuiBaDiDiTestClick2PageHandler),
    (r"/activity/duibaddcpc3", channel.duiba.DuiBaDiDiTestClick3PageHandler),
    (r"/activity/duibaddcpc4", channel.duiba.DuiBaDiDiTestClick4PageHandler),
    (r"/activity/duibaddcpc5", channel.duiba.DuiBaDiDiTestClick5PageHandler),
    (r"/activity/duibaddcpc6", channel.duiba.DuiBaDiDiTestClick6PageHandler),
    (r"/activity/duibaddcpc7", channel.duiba.DuiBaDiDiTestClick7PageHandler),
    (r"/activity/duibaddcpc8", channel.duiba.DuiBaDiDiTestClick8PageHandler),
    (r"/activity/duibaddcpc9", channel.duiba.DuiBaDiDiTestClick9PageHandler),
    (r"/activity/duibaddcpc10", channel.duiba.DuiBaDiDiTestClick10PageHandler),
    (r"/activity/duibaxcq1", channel.duiba.DuiBaCleanCar1PageHandler),
    (r"/activity/duibaele1", channel.duiba.DuiBaEle1PageHandler),
    (r"/activity/duibaele2", channel.duiba.DuiBaEle2PageHandler),
    (r"/activity/duibazh1", channel.duiba.DuiBaSmartInsurancePageHandler),
    (r"/activity/duibazh2", channel.duiba.DuiBaSmartInsurance2PageHandler),
    (r"/activity/duibahf1", channel.duiba.DuiBaHuaFei1PageHandler),
    (r"/activity/duibahf2", channel.duiba.DuiBaHuaFei2PageHandler),
    (r"/activity/duibasxk1", channel.duiba.DuiBa1Shuxinka),
    (r"/activity/duibasxk2", channel.duiba.DuiBa2Shuxinka),
    (r"/activity/duibapae1", channel.duiba.DuiBaEBankPageHandler),
    (r"/activity/duibaaqy1", channel.duiba.DuiBaIQiYiPageHandler),
    (r"/activity/duibadk2", channel.daikuanwang.DuibaDaiKuanPageHandler),
    (r"/activity/duibapaecpc1", channel.e_bank.DuiBaPae1PageHandler),
    (r"/activity/duibapaecpc2", channel.e_bank.DuiBaPae2PageHandler),
    (r"/activity/duibazhcpc1", channel.zonghe.DuiBaZongHe1PageHandler),
    (r"/activity/duibazhcpc2", channel.zonghe.DuiBaZongHe2PageHandler),
    (r"/activity/duibaxcq2", channel.chediandian.DuiBaCheDianDianPageHandler),
    # (r"/activity/duibasxkcpc1", channel.taikang.DuiBaShuxinka1SuperDesk),
    (r"/activity/duibasxkcpc1", channel.taikang.DuiBaShuxinka2PageHandler),
    (r"/activity/duibasxkddcpc1", channel.taikang.DuiBaShuxinka3PageHandler),
    (r"/activity/duibapacpc1", channel.duiba.DuiBaPinganCpc1PageHandler),
    (r"/activity/duibapaddcpc1", channel.duiba.DuiBaPinganDidiCpc1PageHandler),
    (r"/activity/duibaddh1", channel.duiba.DuiBaDaDuHuiPageHandler),
    (r"/activity/duibaddhddcpc1", channel.duiba.DuiBaDaDuHuiDiDiPageHandler),
    (r"/activity/duibaqgzcpc1", channel.qianguanzi.DuiBaQianGuanZiPageHandler),
    (r"/activity/duibaxjkcpc1", channel.cash_card.DuiBaCashCardPageHandler),
    (r"/activity/duibapaxykcpc1", channel.pingan.DuiBaPinganXinYongKaCPC1PageHandler),
    (r"/activity/duibapaxykcpc2", channel.pingan.DuiBaPinganXinYongKaCPC2PageHandler),
    (r"/activity/duibatpcpc1", channel.duiba.DuiBaTaiPingCPCPageHandler),
    (r"/activity/duibahkjcpc1", channel.duiba.DuiBaHuanKuanJinPageHander),
    # 顺网小说
    (r"/activity/shunwxs45hkj1", channel.taikang.ShunWangXiaoShuoPageHander),
    (r"/activity/shunwxstk1", channel.taikang.ShunWangXiaoShuoShuXinKaPageHander),

    # 今日头条
    (r"/activity/jrttzj1", channel.jrtt.SubstituteJRTTZJPageHandler),
    (r"/activity/jrttzj2", channel.jrtt.SubstituteJRTTZJ2PageHandler),
    (r"/activity/jrttpingan", channel.jrtt.PinganJinRiTaoTiaoPageHandler),
    (r"/activity/jrttpingan1", channel.jrtt.PinganJinRiTaoTiao1PageHandler),
    (r"/activity/jrttpingan2", channel.jrtt.PinganJinRiTaoTiao2PageHandler),
    (r"/activity/jrttpingan3", channel.jrtt.PinganJinRiTaoTiao3PageHandler),
    (r"/activity/jrttpingan4", channel.jrtt.PinganJinRiTaoTiao4PageHandler),
    (r"/activity/jrttfcb1", channel.jrtt.JinRiTouTiaoPageHander),
    (r"/activity/jrttfcb2", channel.jrtt.JinRiTouTiaoPageHander2),
    (r"/appointment/jrtttkyy_first", channel.jrtt.AppointmentTKJinRiTouTiaoFirst),
    (r"/appointment/jrtttkyy_second", channel.jrtt.AppointmentTKJinRiTouTiaoSecond),
    (r"/activity/jrttdd", channel.jrtt.SurveyDidiJinRiTouTiao),
    (r"/activity/jrttdd2", channel.jrtt.SurveyDidiJinRiTouTiao2),
    (r"/activity/jrttdd3", channel.jrtt.SurveyDidiJinRiTouTiao3),
    (r"/activity/jrttuber", channel.jrtt.SurveyUberTodayNewsPageHandler),
    (r"/activity/jrttzh1", channel.zonghe.JinRiTouTiaoZongHe1PageHandler),
    (r"/activity/jrttzh2", channel.zonghe.JinRiTouTiaoZongHe2PageHandler),
    (r"/activity/jrttzh3", channel.zonghe.JinRiTouTiaoZongHe3PageHandler),
    (r"/activity/jrttzh5", channel.zonghe.JinRiTouTiaoZongHe5PageHandler),
    (r"/activity/jrttzh6", channel.duiba.JinRiTouTiaoEBankPageHandler),
    (r"/activity/jrttpa1", channel.pinzhong.JinRiTouTiaoPa1PageHandler),
    (r"/activity/jrttpa2", channel.pinzhong.JinRiTouTiaoPa2PageHandler),
    (r"/activity/jrttpa3", channel.pinzhong.JinRiTouTiaoPa3PageHandler),
    (r"/activity/jrttsxk1", channel.taikang.JinRiTouTiaoShuxinka1SuperDesk),
    (r"/activity/jrttsxk2", channel.taikang.JinRiTouTiaoShuxinka2SuperDesk),
    (r"/activity/jrttsxk3", channel.taikang.JinRiTouTiaoShuxinka3SuperDesk),
    (r"/activity/(jrttcp[1-2])", channel.lottery.JinRiTouTiaoCaiPiaoPageHandler),
    # 仁合天泽
    (r"/activity/renhtzdd1", channel.duiba.RenHeTianZePageHandler),
    # 娃哈哈
    (r"/activity/wahhqgz", channel.qianguanzi.WaHaHaQianGuanZiPageHandler),
    (r"/activity/wahhtk", channel.taikang.WaHaHaShuxinkaPageHandler),
    (r"/activity/wahhgq1", channel.taikang.WaHaHaGuoQingPageHander),
    # 微赛
    (r"/activity/weissxk1", channel.taikang.WeiSaiShuxinkaPageHandler),

    # 广点通
    (r"/activity/guangdttk", channel.taikang.GuangDianTongTaiKangPageHandler),
    (r"/activity/(guangdtsxkofo[1-4])", channel.pingan_wifi.GuangDianTongShuXinkaOfoPageHandler),
    (r"/activity/(guangdtfcb[1-4])", channel.taikang.GuangDianTongFeiChangBao1PageHandler),
    (r"/activity/guangdtdd1", channel.didi.GuangDianTongDiDi1PageHandler),
    (r"/activity/(guangdtgq[1-3])", channel.taikang.GuangDianTongGuoQingPageHander),

    # 娃哈哈福礼惠
    (r"/activity/wahhpalx", channel.pingan.WaHaHaPingAnFuLiHuiPageHandler),

    # 渠道作假，暂停
    #(r"/activity/llbpady", channel.pingan.PinganLLBDDPageHandler),
    (r"/activity/ggnpa", channel.pingan.PinganGuGuBirdPageHandler),
    (r"/activity/zsgjdy1", channel.pingan.PinganZSGJ1PageHandler),
    (r"/activity/market_pa", channel.pingan.HeiniuPAPageHandler),
    (r"/activity/txpingan", channel.pingan.PinganCommenNetworkPageHandler),
    (r"/activity/58wzpa", channel.pingan.Pingan58PingAnWeiZhangPageHandler),
    (r"/activity/sypady", channel.pingan.PinganQuickPayPageHandler),
    (r"/activity/gtpingan", channel.pingan.PinganOuAiPageHandler),
    (r"/activity/tzdwxpa1", channel.pingan.YuWenWeiXinPageHandler),


    # 泰康舒心卡
    (r"/activity/taikang_sxk", channel.taikang.TaikangShuxinka),
    (r"/activity/tksxk_sd", channel.taikang.TaikangShuxinkaSuperDesk),
    (r"/activity/ywsxk1", channel.taikang.TaikangShuxinkaYuWen),
    (r"/activity/wpstkzh1", channel.taikang.TaikangShuxinkaSuperDesk),
    # 兴民保险
    (r"/activity/xingminsxk1", channel.taikang.XingMinShuXinKaPageHandler),
    (r"/activity/xingminhtb1", channel.taikang.XingMinBaoXianChuXingPageHander),
    # 智慧旅行
    (r"/activity/zhihuidaoyou", channel.taikang.ZhiHuiQuNaErShuXinKaPageHander),
    # 洗车
    (r"/activity/xiche", channel.xiche.CleanCarPageHandler),
    (r"/activity/ywxcq1", channel.xiche.CleanCarYuWenPageHandler),
    # 木仓科技
    (r"/activity/jkbdpa1", channel.channel_no_idno.JiaKaoBaoDianPageHandler),
    (r"/activity/jkbdmt1", channel.duiba.MuCangDiDiPageHandler),

    # 没有输入身份证号的渠道
    (r"/activity/txgtdd2_noid", channel.channel_no_idno.SurveyTieXiPageHandler),
    (r"/activity/58pady", channel.channel_no_idno.Pingan58PingAnDiaoYanPageHandler),
    (r"/activity/pingan", channel.channel_no_idno.PinganNoIdPageHandler),
    (r"/activity/sdpa1", channel.channel_no_idno.PinganShenDengPageHandler),
    (r"/activity/czwypa1", channel.channel_no_idno.PinganCZWYPageHandler),


    # DDH
    (r"/activity/daduhui", channel.daduhui.SurveyDDHPageHandler),
    (r"/activity/ddh_direct", channel.daduhui.SurveyDdhDirectPageHandler),
    # (r"/activity/ddh_new", channel.daduhui.SurveyDDHNewPageHandler),
    (r"/activity/ywddh1", channel.daduhui.SurveyYuWenPageHandler),
    (r"/activity/ddh", channel.daduhui.DaDuHuiPageHandler),

    # 美华美依
    (r"/appointment/clothes", channel.clothes.SurveyClothesPageHandler),

    # 平安网银
    (r"/activity/ebank", channel.e_bank.EBankPageHandler),
    (r"/activity/ebank1", channel.e_bank.EBank1PageHandler),
    (r"/activity/weixinpae1", channel.e_bank.WeiXinEBankPageHandler),
    (r"/activity/hbrlebank", channel.e_bank.HongBaoEBankPageHandler),
    (r"/activity/wcpae1", channel.e_bank.WaCaiEBankPageHandler),
    (r"/activity/mmpae1", channel.e_bank.MengMaPageHandler),

    # 微车
    (r"/activity/wcpa1", channel.weiche.SmallCarPageHandler),
    (r"/activity/wcdjq1", channel.weiche.SmallCarDiDiPageHandler),
    (r"/activity/wczh1", channel.weiche.SmallCarSmartInsurancePageHandler),
    (r"/activity/weicfcb1", channel.taikang.WeiCheFeiChangBaoPageHandler),

    # 爱卡汽车
    (r"/activity/xcarsxk1", channel.xcar.XCarShuxinka),
    (r"/activity/xcarzh1", channel.xcar.XCarsPageHandler),
    (r"/activity/xcarzj1", channel.xcar.SubstituteXCarPageHandler),

    # 综合页面
    (r"/activity/ywzh1", channel.zonghe.YuWenSmartInsurancePageHandler),
    (r"/activity/sdzh1", channel.zonghe.ShenDengSmartInsurancePageHandler),
    (r"/activity/58zh1", channel.zonghe.WeiZhangSInsurancePageHandler),
    (r"/activity/58zh2", channel.zonghe.WeiZhangSInsurance2PageHandler),
    (r"/activity/58zh3", channel.zonghe.WeiZhangSInsurance3PageHandler),
    (r"/activity/58tczh1", channel.zonghe.TongCheng1PageHandler),
    (r"/activity/58tczh2", channel.zonghe.TongCheng2PageHandler),
    (r"/activity/szzczh1", channel.zonghe.ShenZhouSInsurance1PageHandler),
    (r"/activity/ddcxzh1", channel.zonghe.DiDiZongHePageHandler),
    (r"/activity/hbrlzh1", channel.zonghe.HongBaoZongHePageHandler),
    (r"/activity/chelunzh1", channel.zonghe.CheLunZongHePageHandler),
    (r"/activity/tongxiangzh1", channel.zonghe.TongXiangZongHePageHandler),
    (r"/activity/zhongxinzh1", channel.zonghe.ZhongXinZongHe1PageHandler),
    (r"/activity/zhongxinzh2", channel.zonghe.ZhongXinZongHe2PageHandler),
    (r"/activity/zhongxinzh3", channel.zonghe.ZhongXinZongHe3PageHandler),
    (r"/activity/zhongxinzh4", channel.zonghe.ZhongXinZongHe4PageHandler),
    (r"/activity/zhongxinzh5", channel.zonghe.ZhongXinZongHe5PageHandler),
    (r"/activity/zhongxinzh6", channel.zonghe.ZhongXinZongHe6PageHandler),
    (r"/activity/mjtqzh1", channel.zonghe.MoJiWeatherPageHandler),
    (r"/activity/mjtqzh2", channel.zonghe.MoJiWeather2PageHandler),
    (r"/activity/mjtqzh3", channel.zonghe.MoJiWeather3PageHandler),
    (r"/activity/czwyzh1", channel.zonghe.CheZhuWuYouPageHandler),
    (r"/activity/zsgjzh1", channel.zonghe.BusOfHandPageHandler),
    (r"/activity/yxzh1", channel.zonghe.YouXinPageHandler),
    (r"/activity/tusizh1", channel.zonghe.TuSiPageHandler),
    (r"/activity/wzyhqzh1", channel.zonghe.WanZhongPageHandler),
    (r"/activity/wzyhqzh2", channel.zonghe.WanZhong2PageHandler),
    (r"/activity/wzyhqzh3", channel.zonghe.WanZhong3PageHandler),
    (r"/activity/51dbzh1", channel.zonghe.DuoBao51PageHandler),
    (r"/activity/mozhouzh1", channel.zonghe.MoZhouZongHePageHandler),
    (r"/activity/pasfzh1", channel.zonghe.PingAnSiFangHePageHandler),
    (r"/activity/72zh1", channel.zonghe.QiShiErPageHandler),
    (r"/activity/qnzhcpc1", channel.zonghe.QuNarZongHePageHandler),
    (r"/activity/wpspacx1", channel.zonghe.WPSZongHe1PageHandler),
    (r"/activity/jhsjh1", channel.zonghe.JinHeSuoZongHePageHandler),


    # 多米
    (r"/activity/duomizh1", channel.duomi.DuoMiSInsurance1PageHandler),
    (r"/activity/duomidd1", channel.duomi.SubstituteDuoMiPageHandler),
    (r"/activity/duomipae1", channel.duomi.DuoMiEBankPageHandler),

    # 饿了么页面
    (r"/activity/ywele1", channel.ele.YuWenEle1PageHandler),
    (r"/activity/mjtqele", channel.ele.MoJiWeatherEle1PageHandler),

    # 验证码相关
    (r"/gen/phone_captcha", channel.phone_captcha.HandlerPhoneCaptcha),
    (r"/verify/phone_captcha", channel.phone_captcha.VerifyPhoneCaptcha),
    # 请求现金卡的验证码
    (r"/gen/phone_xjk_captcha", channel.phone_captcha.HandlerXinJinKaPhoneCaptcha),
    # 请求贷款活动的验证码【黑牛有钱】
    (r"/gen/phone_hnyq_captcha", channel.phone_captcha.HeiNiuYouQianPhoneCaptcha),
    # 商城验证码【黑牛商城】
    (r"/gen/phone_shop_captcha", channel.phone_captcha.HeiNiuShangChengPhoneCaptcha),
    # 不展示黑牛信息【专享活动】
    (r"/gen/phone_noheiniu_captcha", channel.phone_captcha.NoHeiNiuPhoneCaptcha),
    # 非100alpha域名用蘑菇保【蘑菇保】
    (r"/gen/phone_mgb_captcha", channel.phone_captcha.MoGuBaoPhoneCaptcha),

    # 善明
    (r"/activity/smpa1", channel.shanming.ShanMingPingAnPageHandler),
    (r"/activity/smpa2", channel.shanming.ShanMingPingAn2PageHandler),
    (r"/activity/smpa3", channel.shanming.ShanMingPingAn3PageHandler),
    (r"/activity/smpa4", channel.shanming.ShanMingPingAn4PageHandler),
    (r"/activity/smpa5", channel.shanming.ShanMingPingAn5PageHandler),
    (r"/activity/smpa6", channel.shanming.ShanMingPingAn6PageHandler),
    (r"/activity/smpa7", channel.shanming.ShanMingPingAn7PageHandler),
    (r"/activity/smpa8", channel.shanming.ShanMingPingAn8PageHandler),
    (r"/activity/smpa9", channel.shanming.ShanMingPingAn9PageHandler),
    (r"/activity/smpa_ten", channel.shanming.ShanMingPingAn10PageHandler),
    (r"/activity/smpa11", channel.shanming.ShanMingPingAn11PageHandler),
    (r"/activity/smpa12", channel.shanming.ShanMingPingAn12PageHandler),
    (r"/activity/smpa13", channel.shanming.ShanMingPingAn13PageHandler),
    (r"/activity/smpa14", channel.shanming.ShanMingPingAn14PageHandler),
    (r"/activity/smpa15", channel.shanming.ShanMingPingAn15PageHandler),
    (r"/activity/smpa16", channel.shanming.ShanMingPingAn16PageHandler),
    (r"/activity/smpa17", channel.shanming.ShanMingPingAn17PageHandler),
    (r"/activity/smpa18", channel.shanming.ShanMingPingAn18PageHandler),
    (r"/activity/smpa19", channel.shanming.ShanMingPingAn19PageHandler),
    (r"/activity/smpa20", channel.shanming.ShanMingPingAn20PageHandler),
    (r"/activity/smzj1", channel.shanming.ShanMingZiJiaPageHandler),
    (r"/activity/smdd1", channel.shanming.ShanMingDiDiPageHandler),
    (r"/activity/smdd2", channel.shanming.ShanMingDiDi2PageHandler),
    (r"/activity/smdd3", channel.shanming.ShanMingDiDi3PageHandler),
    (r"/activity/smdd4", channel.shanming.ShanMingDiDi4PageHandler),
    (r"/activity/smdd5", channel.shanming.ShanMingDiDi5PageHandler),
    (r"/activity/smdd6", channel.shanming.ShanMingDiDi6PageHandler),
    (r"/activity/smdd7", channel.shanming.ShanMingDiDi7PageHandler),
    (r"/activity/smdd8", channel.shanming.ShanMingDiDi8PageHandler),
    (r"/activity/smdd9", channel.shanming.ShanMingDiDi9PageHandler),
    (r"/activity/smzh1", channel.shanming.ShanMingZongHe1PageHandler),
    (r"/activity/smzh2", channel.shanming.ShanMingZongHe2PageHandler),
    (r"/activity/smzh3", channel.shanming.ShanMingZongHe3PageHandler),
    (r"/activity/smzh4", channel.shanming.ShanMingZongHe4PageHandler),
    (r"/activity/smzh5", channel.shanming.ShanMingZongHe5PageHandler),


    # 图片验证码相关
    (r"/gen/image_captcha", image_captcha.HandlerShowCaptchaImage),
    (r"/verify/image_captcha", image_captcha.HandlerVerifyImageCaptcha),
    # 根据手机号判断是否显示手机验证码
    (r"/gen/citybyphone", channel.mobile2city.HandlerMobile2City),

    # 微信合作
    (r"/activity/ddwxservice", channel.didi.SurveyDidiWeiXinServicePageHandler),
    (r"/activity/pawxservice", channel.pingan.WeiXinServiePAPageHandler),

    #汽车之家
    (r"/activity/qczjdd1", channel.car_home.SubstituteCarHomePageHandler),
    (r"/activity/qczjzj1", channel.car_home.SubstituteWifiCarHomePageHandler),

    # 新的edm渠道
    (r"/activity/yedmpa", channel.pingan.PinganYWnewHandler),
    (r"/activity/yedmpa2", channel.pingan.PinganYWnew2Handler),
    (r"/activity/yedmpa3", channel.channel_no_idno.PinganYWnew3Handler),


    # 影视大全
    (r"/activity/ysdqdd", channel.didi.SurveyYingShiDaQuanPageHandler),

    # 神马搜索
    (r"/activity/shenmazh1", channel.shenma.ShenMaZongHePageHandler),
    (r"/activity/shenmapae1", channel.shenma.ShenMaEBankPageHandler),
    (r"/activity/shenmapa1", channel.shenma.ShenMaPingAnPageHandler),
    # 神马
    (r"/activity/shenmatk1", channel.taikang.ShenMaTaiKangPageHander),

    # 搜狗搜索

    (r"/activity/sougouzh1", channel.sougou.SouGouZongHePageHandler),
    (r"/activity/sougoupae1", channel.sougou.SouGouEBankPageHandler),

    # 少儿险
    (r"/activity/child", channel.child.ChildPageHandler),
    (r"/activity/sdpachild", channel.child.ChildShenDengPageHandler),

    # 谷友
    (r"/activity/gymlsdzj1", channel.gooyo.GooYoPageHandler),
    (r"/activity/gooyopa", channel.gooyo.GooYoPinganPageHandler),
    (r"/activity/gooyopa2", channel.gooyo.GooYoPingan2PageHandler),
    (r"/activity/gyzmtqpa1", channel.gooyo.GooYoPingan3PageHandler),
    (r"/activity/gytqtdd", channel.gooyo.GooYoWeatherPageHandler),
    (r"/activity/gyjybzh1", channel.gooyo.GooYoZongHePageHandler),
    (r"/activity/gyjtttzh1", channel.gooyo.GooYoZongHe2PageHandler),
    (r"/activity/gytqtpa", channel.gooyo.GooYoChuXingWeatherPageHandler),
    (r"/activity/gynymbpa1", channel.gooyo.GooYoNuoYaBoMeiPageHandler),
    (r"/activity/139mailzj1", channel.gooyo.GooYo139PageHandler),
    (r"/activity/gykdbpa1", channel.gooyo.GooYoDuiBaoPageHandler),
    (r"/activity/gyjjxczj1", channel.gooyo.GooYoJJXCPageHandler),
    (r"/activity/gyftwifizh1", channel.gooyo.GooYoFlyZongHePageHandler),
    (r"/activity/gydmpae1", channel.gooyo.GooYoDouMi1PageHandler),
    (r"/activity/gydmpae2", channel.gooyo.GooYoDouMi2PageHandler),
    (r"/activity/gydmpae3", channel.gooyo.GooYoDouMi3PageHandler),
    (r"/activity/gydyxwxpae1", channel.gooyo.GooYoYouXinWuXian1PageHandler),
    (r"/activity/gyfcszh1", channel.gooyo.GooYoGoldTreeHePageHandler),
    (r"/activity/gyfcszh2", channel.gooyo.GooYoGoldTreeHe2PageHandler),
    (r"/activity/gyfcszh3", channel.gooyo.GooYoGoldTreeHe3PageHandler),
    (r"/activity/gynnpae1", channel.gooyo.GooYoNuoNuo1PageHandler),
    (r"/activity/gynnzh1", channel.gooyo.GooYoNNZongHePageHandler),
    (r"/activity/gywnzh1", channel.gooyo.GooYoWNZongHePageHandler),
    (r"/activity/gyystzh1", channel.gooyo.YunShiTongZongHePageHandler),
    (r"/activity/gyyhqzh1", channel.zonghe.GuYouYouHuiQuanZonghePageHandler),
    (r"/activity/gyytszh1", channel.zonghe.GuYouYuanTouShuoZonghePageHandler),
    (r"/activity/gyrylzh1", channel.zonghe.RongYiLianZonghePageHandler),
    (r"/activity/gygshzh1", channel.zonghe.GuangShanHuiZongHePageHandler),
    (r"/activity/gybbym1", channel.pingan_vaccines.GuYouBaoBeiYiMiaoPageHandler),
    (r"/activity/gypnczh1", channel.gooyo.GooYoPiNuoCaoZongHePageHandler),
    (r"/activity/gynwjrpae1", channel.e_bank.GuYouNiWoJingRongEBank1PageHandler),
    (r"/activity/gynwjrpae2", channel.e_bank.GuYouNiWoJingRongEBank2PageHandler),
    (r"/activity/gyaabashi", channel.zonghe.GuYouAaBashiPageHandler),
    (r"/activity/gykoudlz1", channel.pingan.GuYouKouDaiLiZiPageHandler),
    (r"/activity/gykoudt3hy", channel.zonghe.GuYouKouDaiTongZhongHePageHandler),
    (r"/activity/gyhongb1", channel.taikang.GuYouHongBaoPageHander),

    # 有股吗
    (r"/activity/gyygmzh1", channel.weiche.GuYouYouGuMaZongHePageHandler),
    (r"/activity/gyygmpae1", channel.e_bank.GuYouYouGuMaEBankPageHandler),

    # 美篇
    (r"/activity/mpdy", channel.meipian.MeiPianDiaoYanPageHandler),
    (r"/activity/mpzh1", channel.meipian.MeiPianHePageHandler),

    # 使用蘑菇保域名
    (r"/activity_mgb/duibaddcpc1", channel.duiba.DuiBaDiDiTestClick1PageHandler_MGB),
    (r"/activity_mgb/duibaddcpc2", channel.duiba.DuiBaDiDiTestClick2PageHandler_MGB),
    (r"/activity_mgb/duibaddcpc3", channel.duiba.DuiBaDiDiTestClick3PageHandler_MGB),
    (r"/activity_mgb/pasfalppa1", channel.channel_no_idno.PinganShenFengPageHandler),

    # 推啊 使用蘑菇保域名
    (r"/activity_mgb/tuiahkjcpc1", channel.tuia.TuiaHuanKuanJinPageHander),
    (r"/activity_mgb/tuiaddcpc1", channel.tuia.TuiADiDiTestClick1PageHandler_MGB),
    (r"/activity_mgb/tuiaddcpc2", channel.tuia.TuiADiDiTestClick2PageHandler_MGB),
    (r"/activity_mgb/(tuiaddcpc[34])", channel.tuia.TuiADiDiTestClick3PageHandler_MGB),
    (r"/activity_mgb/(tuiady(?:2|3|))", channel.tuia.TuiAPingAnDiaoYanPageHandler),
    (r"/activity_mgb/(tuiadk[1-3])", channel.daikuanwang.TuiASuDaiZhiJiaPageHandler),
    (r"/activity_mgb/tuialc1", channel.qianguanzi.TuiAMoGuBaoQianGuanZiPageHandler),
    (r"/activity_mgb/tuiaqm", channel.tuia.TuiAZhonghePageHandler),
    (r"/activity_mgb/tuiaddcpcnew1", channel.bianxianmao.TuiaDiDiDiCPCNew1PageHandler),
    (r"/activity_mgb/tuiameituan1", channel.tuia.TuiAMeiTuanTaiKangPageHandler),
    (r"/activity_mgb/tuiameituan2", channel.tuia.TuiAMeiTuan2PageHandler),

    # 宇闻平安新页面 使用蘑菇保域名
    (r"/activity_mgb/ywpa1", channel.channel_no_idno.PinganYuWenPageHandler),
    (r"/activity_niorv/ywpa1", channel.channel_no_idno.PinganYuWenPageHandler),

    # 话费
    (r"/activity/huafei", channel.huafei.HuaFeiPageHandler),
    (r"/activity/ywhf1", channel.huafei.YuWenHuaFei1PageHandler),
    (r"/activity/ywhf2", channel.huafei.YuWenHuaFei2PageHandler),
    (r"/activity/duanxin", channel.huafei.DuanXinPageHandler),

    # T微信
    (r"/activity/twxtk1", channel.tweixin.TWeiXinFeiChangBaoPageHandler),
    (r"/activity/twxpa1", channel.tweixin.TWeiXinPAPageHandler),
    (r"/activity/twxpa2", channel.tweixin.TWeiXinPA2PageHandler),


    # 酷滑
    (r"/activity/khspdy", channel.kuhua.PinganCoolSlidePageHandler),
    (r"/activity/khspdy2", channel.kuhua.PinganCoolSlide2PageHandler),
    (r"/activity/khspdy3", channel.kuhua.PinganCoolSlide3PageHandler),
    (r"/activity/khsphf1", channel.kuhua.CoolSlideHuaFei1PageHandler),
    (r"/activity/khspzh1", channel.kuhua.CoolSlideZongHe1PageHandler),

    # 抽奖
    (r"/activity/forward", channel.forward.Forward),
    (r"/activity/pawififorward", channel.forward.PaWifiForward),
    (r"/activity/189llforward", channel.forward.PaWifiForward),
    (r"/activity/forward/phone", channel.forward.UpdateForwardPhoneHandler),
    (r"/activity/pawifijdforward", channel.forward.JingDongKaForwardHandler),
    (r"/activity/189wxllforward", channel.forward.WeixinLiuLiang189Forward),

    # 平安wifi 相关链接
    (r"/activity/pawifikaola", channel.pingan_wifi.SurveyPingAnWiFiKoalaPageHandler),
    (r"/activity/pawifiym", channel.pingan_wifi.PinganWiFiYMPageHandler),
    (r"/activity/pawifiym1", channel.pingan_wifi.PinganWiFi1YMPageHandler),
    (r"/activity/pawifizj", channel.pingan_wifi.PinganWiFiZJPageHandler),
    (r"/activity/pawifizj1", channel.pingan_wifi.PinganWiFiZJ1PageHandler),
    (r"/activity/pawificlzj", channel.pingan_wifi.PinganWiFiCLZJPageHandler),
    (r"/activity/pawifidd", channel.pingan_wifi.PinganWiFiDDOptimizationPageHandler),
    (r"/activity/pawifidd1", channel.pingan_wifi.PinganWiFiDD1PageHandler),
    (r"/activity/pawifidd2", channel.pingan_wifi.PinganWiFiDD2PageHandler),
    (r"/activity/pawifisyb", channel.pingan_wifi.PinganShouYiBaoPageHandler),
    (r"/activity/pawifidy", channel.pingan_wifi.PinganPingAnDiaoYanPageHandler),
    (r"/activity/pawifihf1", channel.pingan_wifi.WiFiHuaFei1PageHandler),
    (r"/activity/pawifihf2", channel.pingan_wifi.WiFiHuaFei2PageHandler),
    (r"/activity/pawifizh1", channel.pingan_wifi.PingAnWiFiZongHePageHandler),
    (r"/activity/pawificj1", channel.pingan_wifi.PingAnWiFiChouJiangPageHandler),
    (r"/activity/pawifill1", channel.pingan_wifi.PawifilLiuliangPageHandler),
    (r"/activity/pawifill2", channel.pingan_wifi.PawifilLiuliang2PageHandler),
    (r"/activity/pawifill3", channel.pingan_wifi.PawifilLiuliang3PageHandler),
    (r"/activity/pawifijb1", channel.pingan_wifi.PawifilJinBiPageHandler),
    (r"/activity/pawifijb2", channel.pingan_wifi.PawifilJinBi2PageHandler),
    (r"/activity/pawifijb3", channel.pingan_wifi.PawifilJinBi3PageHandler),
    (r"/activity/pawifijd1", channel.pingan_wifi.JingDongPageHandler),
    (r"/activity/pawifiofo1", channel.pingan_wifi.PAWifiOfoPageHandler),
    (r"/activity/189wxll2", channel.pingan_wifi.WeiXin189LiuLiangPageHandler),
    (r"/activity/pawifijb4", channel.pingan_wifi.PawifilJinBi4PageHandler),
    (r"/activity/pawifiofo2", channel.pingan_wifi.PAWifiOfo2PageHandler),
    (r"/activity/pawifizj2", channel.pingan_wifi.PinganWiFiZJ2PageHandler),

    # 商务支持
    (r"/activity/taikangdd1", channel.didi.ShangWuTk1PageHandler),
    (r"/activity/zonghedd1", channel.zonghe.ZongheTk1PageHandler),
    (r"/activity_mgb/taikangdd2", channel.didi.ShangWuTk2PageHandler_MGB),
    # 运营商拦截
    (r"/activity/dkljdd1", channel.pingan_wifi.DaiKuamLanJieDiDiPageHandler),
    # 有众
    (r"/activity/yzdd1", channel.youzhong.YouZhongDiDi1PageHandler),
    (r"/activity/yzebank1", channel.youzhong.YouZhongEBank1PageHandler),

    # 短信保单
    (r"/activity/insurance_msg", channel.insurance_msg.InsuranceMessage),
    # 平安优联
    (r"/activity/payldd1", channel.didi.PingAnYouLianDiDiPageHandler),
    (r"/activity/zndxofo1", channel.taikang.ZhiNengDuanXinOfoPageHander),
    (r"/activity/zndxmobike1", channel.taikang.ZhiNengDuanXinMobikePage1Hander),
    (r"/activity/paylmt1", channel.didi.PingAnYouLianMTaiKangPageHandler),

    # 变现猫
    (r"/activity/(bxmdd[1-3])", channel.bianxianmao.BXMDiDiPageHandler),
    (r"/activity/bxmzh1", channel.bianxianmao.BXMZongHePageHandler),
    (r"/activity/bxmpa1", channel.bianxianmao.BXMPingAnPageHandler),
    (r"/activity/bxmcpcpc1", channel.bianxianmao.BianXianMaoCaiPiaoCPC1PageHandler),
    (r"/activity/bxmdkcpc1", channel.bianxianmao.BianXianMaoDaiKuanPageHandler),
    (r"/activity/bxmqgzcpc1", channel.bianxianmao.BianXianMaoQianGuanZiPageHandler),
    (r"/activity/(bxmtkdd[1-2])", channel.bianxianmao.BianXianMaoTaiKangDiDiPageHandler),
    (r"/activity/bxmdk1", channel.bianxianmao.BianXianMaoYouQianPageHandler),
    (r"/activity/bxmdk2", channel.bianxianmao.BianXianMaoYouQian2PageHandler),
    (r"/activity/bxmtk2", channel.bianxianmao.BianXianMaoTaiKangPage2Handler),
    (r"/activity/bxmtk3", channel.bianxianmao.BianXianMaoTaiKangPage3Handler),
    (r"/activity/bxmloantk1", channel.bianxianmao.BianXianMaoLoanTaiKangPage1Handler),
    # (r"/activity/bxmloanddh1", channel.daduhui.YuWenDaDuHui3PageHandler),
    (r"/activity/bxmloanhz1", channel.bianxianmao.BianXianMaoLoanHeZhongPage1Handler),
    (r"/activity/bxmloanpa1", channel.bianxianmao.BianXianMaoLoanPingAnPage1Handler),
    (r"/activity/bxmddcpc1", channel.bianxianmao.BianXianMaoDiDiCPC1Page1Handler),
    (r"/activity/bxmtkcpc1", channel.bianxianmao.BianXianMaoTaiKangCPC1Page1Handler),
    (r"/activity/bxmmt1", channel.bianxianmao.BianXianMaoMeiTuanPageHandler),

    # 变现猫转盘综合链接
    (r"/activity/bxmzpzh1", channel.bianxianmao.BianXianMaoZhuanPanPageHandler),


    # 快兑宝
    (r"/activity/kdbebank1", channel.kuaiduibao.KDBEBankPageHandler),
    (r"/activity/kdbdd1", channel.kuaiduibao.KDBDiDiPageHandler),
    (r"/activity/kdbdy1", channel.kuaiduibao.KDBPingAnDiaoYanPageHandler),
    (r"/activity/kdbzj1", channel.kuaiduibao.KDBZJPageHandler),
    (r"/activity/kdbzh1", channel.kuaiduibao.KDBZongHePageHandler),
    (r"/activity/kdbfcb1", channel.kuaiduibao.KDBFeiChangBaoPageHander),

    # 泰康测保
    (r"/activity/calculate_taikang", channel.calculate_taikang.CalculatePremiumTaiKang),
    (r"/activity/appoinment_taikang", channel.calculate_taikang.AppointmentTaiKang),
    # 推吧
    (r"/activity/tuibaddcpc1", channel.duiba.TuiBaDiDiCPCPageHandler),
    (r"/activity/(tuibadd[2-5])", channel.duiba.TuiBaDiDiCPCPage2Handler),

    # 发送短信提醒
    (r"/sms/remind", insurance.handlers.insurance_remind.InsuranceExpireRemindHandler),

    # 兑吧接口
    (r"/api/insurance/duiba", insurance.channel.interface_duiba.DuibaInterfaceHandler),

    (r"/api/insurance/ypa", insurance.channel.interface_duiba.YpaInterfaceHandler),

    # 海航通信
    (r"/api/insurance/hhtxapi", insurance.channel.interface_duiba.HaiHangTongXinInterfaceHandler),
    (r"/activity/hhtxwc1", channel.daikuanwang.HaiHangTongXinWaCaiPageHandler),

    # 榕时代
    (r"/api/insurance/rsdjiekou1", insurance.channel.interface_duiba.RongShiDaiInterfaceHandler),

    # 单独的领取结果页
    (r"/result_page", insurance.handlers.page_handler.ResultPageHandler),

    # 爱奇艺页面
    (r"/activity/jmmaqy1", channel.iqiyi.JMMIQiYiPageHandler),
    (r"/activity/jmmaqy2", channel.quanmama.QuanMaMaQiyi2PageHandler),
    (r"/activity/jmmaqy3", channel.quanmama.QuanMaMaQiyi3PageHandler),
    (r"/activity/mmaqy1", channel.iqiyi.MMIQiYiPageHandler),
    (r"/activity/pawifiaqy1", channel.iqiyi.PAWIFIQiYiPageHandler),
    (r"/activity/aqyddcpc_page1", channel.duiba.AiQiYiDiDiCPCPageHandler),
    (r"/activity/aqydkcpc1", channel.iqiyi.AiQiYiDaiKuanCPCPageHandler),
    (r"/activity/aqytkcpc1", channel.taikang.AiQiYiTaiKangPageHander),
    (r"/activity/aqymtcpc1", channel.didi.AiQiYiMeiTuanPageHandler),
    # 奥金智策
    (r"/activity/ajzcjdbdk1", channel.iqiyi.AoJinZhiCeJiaDuoBaoDaiKuanPageHandler),
    # 同程
    (r"/activity/ywtc1", channel.tongcheng_travel.TongChengTravelHandler),
    (r"/activity/pawifitc1", channel.tongcheng_travel.PingawifiTongChengPageHandler),

    # 欧朋
    (r"/activity/ope1", channel.oupeng.OuPengEBankPageHandler),
    (r"/activity/opdd1", channel.oupeng.OuPengDDPageHandler),
    (r"/activity/opsxk1", channel.oupeng.OuPengShuxinkaPageHandler),

    # 钱方
    (r"/activity/qfpae1", channel.qianfang.QianFangPaePageHandler),
    (r"/activity/qfzh1", channel.qianfang.QianFangZonghePageHandler),
    (r"/activity/jmmzh1", channel.zonghe.QuanMaMa1ZonghePageHandler),
    (r"/activity/jmmzh2", channel.zonghe.QuanMaMa2ZonghePageHandler),
    (r"/activity/jmmzh3", channel.zonghe.QuanMaMa3ZonghePageHandler),

    # 114挂号
    (r"/activity/114ghzh1", channel.guahao114.GuaHao114ZongHePageHandler),
    (r"/activity/114ghsxk1", channel.guahao114.GuaHao114ShuXinKaPageHandler),

    # 贷款
    (r"/activity/loan", channel.daikuanwang.DaiKuanWangPageHandler),
    (r"/activity/loan2", channel.daikuanwang.JieKuanZhuangJiaPageHandler),
    (r"/activity/duibapaph1", channel.daikuanwang.PaPuHuiDaiKuanPageHandler),
    (r"/activity/duibawc1", channel.daikuanwang.PaWaCaiDaiKuanPageHandler),
    (r"/activity/duibasdcpc1", channel.daikuanwang.DuiBaSuDaiZhiJiaPageHandler),

    # 第五传媒
    (r"/activity/d5dd1", channel.didi.DiWuChuanMeiPageHandler),
    (r"/activity/d5e1", channel.e_bank.DiWuE1PageHandler),
    (r"/activity/d5sxk1", channel.taikang.DiWuShuXinKaPageHandler),
    (r"/activity/d5jh1", channel.zonghe.DiWuChuanMeiZhongHePageHandler),

    # 瑞狮
    (r"/activity/rse1", channel.ruishi.RuiShiPageHandler),

    # 钱箱
    (r"/activity/qxjdzh1", channel.zonghe.QiangXiangZongHePageHandler),
    (r"/activity/qxjdebank1", channel.e_bank.QianXiangPageHandler),


    # 中保金服务
    (r"/activity/zbddbszh1", channel.zhongbaojinfu.ZhongBaoJinFuPageHandler),

    # 佰联钱包
    (r"/activity/bldd1", channel.didi.BaiLianQianBaoPageHandler),
    (r"/activity/bljh1", channel.zonghe.BaiLianQianBaoZongHePageHandler),

    # 二十一世纪医院
    (r"/activity/gyyysxk1", channel.taikang.ErShiYiShiJiYiYuanPageHandler),
    # 掌众科技
    (r"/activity/sjjkpae1", channel.e_bank.ZhangZhongKeJiPAEPageHandler),
    # 家有宝宝
    (r"/activity/jybbzh1", channel.zonghe.JiaYouBaoBaoZonghePageHandler),

    # 有利网
    (r"/activity/ylwzh1", channel.zonghe.YouLiWangZonghePageHandler),
    (r"/activity/ylwdd1", channel.duiba.YouLiWang1PageHandler),
    (r"/activity/ylwdd2", channel.duiba.YouLiWang2PageHandler),
    (r"/activity/ylwdd3", channel.duiba.YouLiWang3PageHandler),
    (r"/activity/ylwdd4", channel.duiba.YouLiWang4PageHandler),
    (r"/activity/ylwdd5", channel.duiba.YouLiWang5PageHandler),
    (r"/activity/ylwpae1", channel.e_bank.YouLiWangPae1PageHandler),
    (r"/activity/ylwpae2", channel.e_bank.YouLiWangPae2PageHandler),
    (r"/activity/ylwpae3", channel.e_bank.YouLiWangPae3PageHandler),
    (r"/activity/ylwcp1", channel.lottery.YouLiWangCaiPiao1PageHandler),
    (r"/activity/ylwcp2", channel.lottery.YouLiWangCaiPiao2PageHandler),
    (r"/activity/ylwcp3", channel.lottery.YouLiWangCaiPiao3PageHandler),

    # 光卡
    (r"/activity/yfcb1", channel.taikang.GuangKaPageHandler),
    (r"/activity/yedmloan1", channel.daikuanwang.GuangKaDaiKuanPageHandler),
    (r"/activity/yedmzh1", channel.zonghe.GuangKaZonghePageHandler),
    (r"/activity/yedmxcq1", channel.chediandian.GuangKaPageHandler),

    # 中烟代理
    (r"/activity/zhongydlfcb", channel.taikang.ZhongYanDaiLiFeiChangBaoKaPageHandler),
    # 选婷
    (r"/activity/xtdd1", channel.didi.XuanTingPageDiDiHandler),
    (r"/activity/xtjh1", channel.zonghe.XuanTingZhonHePageHandler),
    (r"/activity/xtsxk1", channel.taikang.XuanTingShuxinkaSuperDesk),

    # 树熊
    (r"/activity/sxwifizh1", channel.zonghe.ShuXiongZonghePageHandler),
    (r"/activity/sxwifipae1", channel.e_bank.ShuXiongPaePageHandler),

    # 宏禧聚信
    (r"/activity/hxjxdk1", channel.daikuanwang.HongXiJuXinDK1PageHandler),
    (r"/activity/hxjxpa1", channel.pinzhong.HongXiJuXinPa1PageHandler),
    (r"/activity/hxjxpa2", channel.pinzhong.HongXiJuXinPa2PageHandler),

    # 临点
    (r"/activity/ldjh1", channel.zonghe.LinDianZongHe1PageHandler),
    # 爱普
    # (r"/activity/aipu", channel.bianxianmao.AiPuPageHandler),
    (r"/activity/aipu", channel.taikang.AiPuPageHandler),
    (r"/activity/taikang_aipu", channel.taikang.TaiKangAiPuPageHander),
    # 72变
    (r"/activity/72guoq1", channel.taikang.GuoQing72BianPageHander),

    # 一元淘米
    (r"/activity/tmebank1", channel.e_bank.YiYuanTaoMiPageHandler),
    (r"/activity/tmzh1", channel.zonghe.YiYuanTaoMiZongHePageHandler),

    # JJ学车
    (r"/activity/gyjjxczh1", channel.zonghe.JJXueCheZongHePageHandler),

    # 北京联通114挂号
    (r"/activity/ltghsxk1", channel.taikang.LianTongGuaHaoPageHandler),
    (r"/activity/ltghsxk2", channel.taikang.LianTong114GuaHaoShuxinka1SuperDesk),
    (r"/activity/ltghpa1", channel.pingan.DuiBaPinganLianTong114GuaHaoPageHandler),

    # 挖财
    (r"/activity/wcpae2", channel.e_bank.WaCai2EBankPageHandler),
    (r"/activity/wcpae3", channel.e_bank.WaCai3EBankPageHandler),
    (r"/activity/wcpae4", channel.e_bank.WaCai4EBankPageHandler),
    (r"/activity/wcpae5", channel.e_bank.WaCai5EBankPageHandler),
    (r"/activity/wacxyktk1", channel.taikang.WaCaiXinYongKaTaiKangPageHander),

    # 智汇推
    (r"/activity/zhtdc1", channel.pingan.PinganZhiHuiTuiDiaoCha1PageHandler),
    (r"/activity/(zhtdc[2-6])", channel.channel_no_idno.PinganZhiHuiTuiDiaoCha2PageHandler),
    (r"/activity/zhtym1", channel.pingan_vaccines.ZhiHuiTuiYiMiaoPageHandler),

    # 车友会
    (r"/activity/cheyouhui", channel.cheyouhui.CheYouHuiPageHandler),

    # 信用钱包
    (r"/activity/xyqbpae1", channel.e_bank.XinYongQianBaoPaePageHandler),
    (r"/activity/xyqbzh1", channel.zonghe.XinYongQianBaoZonghePageHandler),
    (r"/activity/xinyqb1", channel.xyqianbao.XinYongQianBaoPageHandler),
    (r"/xinyong/count", channel.xyqianbao.CounterClickHandler),

    # 简单借款
    (r"/activity/jiandpae1", channel.e_bank.JianDanJieKuanPageHandler),

    # 券妈妈
    (r"/activity/jmmpaph1", channel.daikuanwang.QuanMaMaPageHandler),
    (r"/activity/jmmxcq1", channel.chediandian.QuanMaMaCheDianDianPageHandler),
    (r"/activity/quanmmt1", channel.didi.QuanMaMaTaiKangPageHandler),
    # 聚信互联
    (r"/activity/(juxhlmt[1-6])", channel.didi.JuXinHuLianMeiTuanTaiKangPageHandler),
    (r"/activity/(juxhldd[1-2])", channel.duiba.JuXinHuLianDiDiPageHandler),
    (r"/activity/(juxhlhkj[12])", channel.duiba.JuXinHuLianHuanKuanJinPageHander),
    # 蜂巢云
    (r"/activity/fcyhkj1", channel.taikang.FengChaoYunHuanKuanJinPageHander),
    (r"/activity/fcymt1", channel.didi.FengChaoYunMeiTuanPageHandler),

    # 百传
    (r"/activity/bcdd1", channel.didi.BaiChuanDidiPageHandler),
    (r"/activity/bcqq1", channel.qq.BaiChuanQQPageHandler),

    # 泊安
    (r"/activity/gybazh1", channel.zonghe.BoAnZongHe1PageHandler),

    # 袋袋付
    (r"/activity/ddfpae1", channel.e_bank.DaiDaiFuPae1PageHandler),
    (r"/activity/ddfpae2", channel.e_bank.DaiDaiFuPae2PageHandler),
    (r"/activity/ddfpae3", channel.e_bank.DaiDaiFuPae3PageHandler),
    (r"/activity/ddfpae4", channel.e_bank.DaiDaiFuPae4PageHandler),
    (r"/activity/ddfpae5", channel.e_bank.DaiDaiFuPae5PageHandler),
    (r"/activity/ddfzh1", channel.tv_yaoyiyao.DaiDaiFuZongHe1PageHandler),

    # 轻松借
    (r"/activity/qsjpae1", channel.e_bank.QingSongJiePageHandler),

    # 神灯
    (r"/activity/sdztpa1", channel.channel_no_idno.ShenDengZhiTouPageHandler),

    # 宇闻
    (r"/activity/ywxcq2", channel.chediandian.YuWenPageHandler),
    (r"/activity/ywlxsfcb1", channel.taikang.YuWenLvXingSheFeiChangBao1PageHandler),
    (r"/activity/ywlxsfcb2", channel.taikang.YuWenLvXingSheFeiChangBao2PageHandler),
    (r"/activity/ywddh3", channel.daduhui.YuWenDaDuHui3PageHandler),
    (r"/activity/ywpaxyk1", channel.pingan.YuWenPinganXinYongKaCPC1PageHandler),
    (r"/activity/ywddh2", channel.duiba.YuWenDaDuHui2PageHandler),
    (r"/activity/ywofo1", channel.pingan_wifi.YuWenOfoPageHandler),
    (r"/activity/ywtk1", channel.taikang.YuWenTaiKangPageHander),
    (r"/activity/ywhkj1", channel.taikang.YuWenHuanKuanJinPageHander),
    (r"/activity/ywmt1", channel.didi.YuWenMeiTuanTaiKangPageHandler),
    (r"/activity/(sbqtk[1-3])", channel.taikang.ShiBoQinTaiKangPageHander),
    # 钱包金福
    (r"/activity/qianbjf1", channel.taikang.QianBaoJinFuTaiKangPageHander),
    # 联通
    (r"/activity/lttk1", channel.taikang.LianTongTaiKangPageHander),
    (r"/activity/ltpae1", channel.e_bank.LianTongPageHandler),
    # 黑牛
    (r"/activity/heiniucxq1", channel.chediandian.HeiniuPageHandler),
    (r"/activity/hnmobai1", channel.pingan_wifi.HeiNiuMoBaiPageHandler),
    # 到位
    (r"/activity/daowpae1", channel.e_bank.DaoWeiPAEPageHandler),
    (r"/activity/daowtk1", channel.taikang.DaoWeiTaiKangPageHander),
    (r"/activity/daowsxk1", channel.taikang.DaoWeiShuXinKaPageHandler),
    (r"/activity/daowpa1", channel.pingan.DaoWeiPingAnPageHandler),
    (r"/activity/daowzh1", channel.weiche.DaoWeiZongHe1PageHandler),
    # 闪银
    (r"/activity/sypae1", channel.e_bank.ShanYinPageHandler),
    (r"/activity/syddh1", channel.daduhui.ShanYinDDH1PageHandler),
    (r"/activity/sysxk1", channel.taikang.ShanYinSXK1PageHandler),
    (r"/activity/syhz1",channel.duiba.ShanYinHeZhong1PageHandler),
    (r"/activity/sypa1", channel.pingan.ShanYinPinAn1PageHandler),
    (r"/activity/syyd1", channel.pingan.ShanYinYunDong1PageHandler),
    (r"/activity/sytk1", channel.taikang.ShanYinTaiKangPageHander),
    (r"/activity/sydd1", channel.duiba.ShanYinDiDiCPCPageHandler),

    # 沙发管家
    (r"/activity/sfgj1", channel.taikang.ShaFaGuanJiaPage1Hander),

    # 网易新闻
    (r"/activity/wyxwpae1", channel.e_bank.WangYiXinWenPAE1PageHandler),
    (r"/activity/wyxwpae2", channel.e_bank.WangYiXinWenPAE2PageHandler),
    (r"/activity/wyxwzh1", channel.zonghe.WangYiXinWenZongHe1PageHandler),
    (r"/activity/wyxwzh2", channel.zonghe.WangYiXinWenZongHe2PageHandler),
    (r"/activity/wyxwpa1", channel.pingan.WangYiXinWenPa1PageHandler),
    (r"/activity/wyxwpa2", channel.pingan.WangYiXinWenPa2PageHandler),
    (r"/activity/wyxwddh1", channel.duiba.WangYiXinWenDaDuHui1PageHandler),
    (r"/activity/wyxwddh2", channel.duiba.WangYiXinWenDaDuHui2PageHandler),
    (r"/activity/wyxwddh3", channel.duiba.WangYiXinWenDaDuHui3PageHandler),
    (r"/activity/wyxwpa3", channel.duiba.WangYiXinWenPingAn3PageHandler),
    (r"/activity/wyxwpa4", channel.duiba.WangYiXinWenPingAn4PageHandler),
    (r"/activity/wyxwpa5", channel.duiba.WangYiXinWenPingAn5PageHandler),
    (r"/activity/wyxwsxk1", channel.taikang.WangYiXinWenShuxinka1SuperDesk),
    (r"/activity/wyxwsxk2", channel.taikang.WangYiXinWenShuxinka2SuperDesk),
    (r"/activity/wyxwsxk3", channel.taikang.WangYiXinWenShuxinka3SuperDesk),
    (r"/activity/(wyxwdk[1-2])", channel.daikuanwang.WangYiXinWenDaiKuanPageHandler),

    # 花生Wi-Fi
    (r"/activity/hse1", channel.e_bank.HuaShengEBackPageHandler),
    (r"/activity/hsdj1", channel.zonghe.HuaShengDJPageHandler),

    # 网氪
    (r"/activity/wkxccx1", channel.xiche.WangKeXiCheChuXingPageHandler),
    (r"/activity/wkcx1", channel.taikang.WangKeChuXingPageHandler),

    # 网易有道
    (r"/activity/wyydpae1", channel.duiba.WangYiYouDaoEBankPageHandler),
    (r"/activity/wyydpae2", channel.duiba.WangYiYouDaoEBank2PageHandler),
    (r"/activity/wyydpae3", channel.duiba.WangYiYouDaoEBank3PageHandler),
    (r"/activity/wyydpae4", channel.duiba.WangYiYouDaoEBank4PageHandler),
    (r"/activity/wyydpae5", channel.duiba.WangYiYouDaoEBank5PageHandler),
    (r"/activity/wyydzh1", channel.zonghe.WangYiYouDaoZongHePageHandler),
    (r"/activity/wyydzh2", channel.zonghe.WangYiYouDaoZongHe2PageHandler),
    (r"/activity/wyydzh3", channel.zonghe.WangYiYouDaoZongHe3PageHandler),
    (r"/activity/wyydzh4", channel.zonghe.WangYiYouDaoZongHe4PageHandler),
    (r"/activity/wyydzh5", channel.zonghe.WangYiYouDaoZongHe5PageHandler),
    (r"/activity/wyydpa1", channel.pinzhong.WangYiYouDaoPa1PageHandler),
    (r"/activity/wyydpa2", channel.pinzhong.WangYiYouDaoPa2PageHandler),
    (r"/activity/wyydpa3", channel.pinzhong.WangYiYouDaoPa3PageHandler),
    (r"/activity/wyydpa4", channel.pinzhong.WangYiYouDaoPa4PageHandler),
    (r"/activity/wyydpa5", channel.pinzhong.WangYiYouDaoPa5PageHandler),
    (r"/activity/(wyyddk[1-5])", channel.daikuanwang.WangYiYouDaoDaiKuanPageHandler),

    # 随行付
    (r"/activity/sxfzh1", channel.tv_yaoyiyao.SuiXingFuZongHe1PageHandler),
    (r"/activity/sxfpa1", channel.duiba.SuiXingFuPinganPageHandler),
    (r"/activity/sxfpae1", channel.e_bank.SuiXingFuPingAnEBankPageHandler),

    # 合众
    (r"/activity/duibahzddcpc1",channel.duiba.HeZhongDiDiPageHandler),
    (r"/activity/duibahz1",channel.duiba.HeZhongPageHandler),
    # 金山
    (r"/activity/(wps[1-2])", channel.zonghe.WPSPageHandler),
    # 百度
    (r"/activity/(baiduad[1-2])", channel.zonghe.BaiDuADPageHandler),
    # 聚汇推
    (r"/activity/(juhuitui[1-2])", channel.zonghe.JuHuiTuiPageHandler),
    (r"/activity/juhuitui3", channel.tv_yaoyiyao.JuHuiTuiPageHandler),
    (r"/activity/juhuitui4", channel.tv_yaoyiyao.JuHuiTuiHuanKuanJinPageHandler),
    # 易生
    (r"/activity/yisheng1", channel.zonghe.YiShengPageHandler),
    # 章鱼移动
    (r"/activity/(zhangyu[13-9])", channel.zonghe.ZhangYuPageHandler),
    (r"/activity/(zhangyu10)", channel.zonghe.ZhangYuPageHandler),
    (r"/activity/zhangyu2", channel.tv_yaoyiyao.ZhangYuPage2Handler),
    (r"/activity/(zhangyu1[1-5])", channel.tv_yaoyiyao.ZhangYuPage2Handler),
    # 139邮箱
    (r"/activity/139yx", channel.zonghe.YouXiang139PageHandler),

    # IN-APP
    (r"/activity/(inapp[1-2])", channel.zonghe.INAPPPageHandler),

    # 189邮箱
    (r"/activity/189mailfcb1",channel.taikang.Mail_189_FeiChangBao1PageHandler),

    # 应用试客
    (r"/activity/yyskym1", channel.pingan_vaccines.YingYongShiKeYiMiaoPageHandler),
    (r"/activity_mgb/(yyskmgb[1-2])", channel.tuia.YingYongShiKePageHandler_MGB),
    (r"/activity/yyskdk1", channel.daikuanwang.YingYongShiKeSuDaiZhiJiaPageHandler),
    (r"/activity/(yyskqmcx[1-2])", channel.zonghe.YingYongShiKeZongHePageHandler),
    (r"/activity/(yyskaxzf[1-2])", channel.duiba.YingYongShiKeEBankPageHandler),

    # 互动推cpc 渠道
    (r"/activity/(hudtcpc[1-2])", channel.lottery.HuDongTuiCPC1PageHandler),
    (r"/activity/hudongtcpc1", channel.duiba.HuDongTuiCPCNewPageHandler),
    (r"/activity/(hudongtcpcdd[12])", channel.duiba.HuDongTuiCPCDiDiNewPageHandler),
    (r"/activity/(hudongtcpchuankj[12])", channel.taikang.HuDongTuiCPCHuanKuanJinPageHander),
    (r"/activity/(hudongtcpcmt[12])", channel.didi.HuDongTuiCPCMeiTuanPageHandler),


    # 中信
    (r"/activity/zhongxin1", channel.zonghe.ZhongXinPageHandler),
    # 平安运动
    (r"/activity/payd1", channel.pingan.PinganYunDong1PageHandler),
    (r"/activity/payd2", channel.pingan.PinganYunDong2PageHandler),
    # 平安自驾
    (r"/activity/pazj1", channel.pingan.PinganZiJiaPageHandler),

    # 腾讯智汇推
    (r"/activity/txzht1", channel.duiba.TengXunZhiHuiTuiEBankPageHandler),
    (r"/activity/txzht5", channel.duiba.TengXunZhiHuiTuiEBank5PageHandler),
    (r"/activity/txzht6", channel.duiba.TengXunZhiHuiTuiEBank6PageHandler),
    (r"/activity/txzht7", channel.duiba.TengXunZhiHuiTuiEBank7PageHandler),
    (r"/activity/txzht8", channel.duiba.TengXunZhiHuiTuiEBank8PageHandler),
    (r"/activity/(txzht10\d{2})", channel.duiba.TengXunZhiHuiTuiEBankPageHandler),

    (r"/activity/txzht2", channel.pinzhong.TengXunZhiHuiTuiPaPageHandler),
    (r"/activity/txzht9", channel.pinzhong.TengXunZhiHuiTuiPa9PageHandler),
    (r"/activity/txzht10", channel.pinzhong.TengXunZhiHuiTuiPa10PageHandler),
    (r"/activity/txzht11", channel.pinzhong.TengXunZhiHuiTuiPa11PageHandler),
    (r"/activity/txzht12", channel.pinzhong.TengXunZhiHuiTuiPa12PageHandler),
    (r"/activity/(txzht20\d{2})", channel.pinzhong.TengXunZhiHuiTuiPaPageHandler),

    (r"/activity/txzht3", channel.zonghe.TengXunZhiHuiTuiZongHePageHandler),
    (r"/activity/txzht13", channel.zonghe.TengXunZhiHuiTuiZongHe13PageHandler),
    (r"/activity/txzht14", channel.zonghe.TengXunZhiHuiTuiZongHe14PageHandler),
    (r"/activity/txzht15", channel.zonghe.TengXunZhiHuiTuiZongHe15PageHandler),
    (r"/activity/txzht16", channel.zonghe.TengXunZhiHuiTuiZongHe16PageHandler),
    (r"/activity/(txzht30\d{2}|txzht17|txzht19|txzht20)", channel.zonghe.TengXunZhiHuiTuiZongHePageHandler),

    (r"/activity/txzht4", channel.channel_no_idno.TengXunZhiHuiTuiPaDyPageHandler),
    (r"/activity/txzht18", channel.channel_no_idno.TengXunZhiHuiTuiPaDy18PageHandler),
    (r"/activity/(txzht40\d{2})", channel.channel_no_idno.TengXunZhiHuiTuiPaDyPageHandler),

    # 微信公众号
    (r"/activity/wxgzh1", channel.duiba.WeiXinGongZhongHaoEBank1PageHandler),
    (r"/activity/(wxgzh[2|5])", channel.pinzhong.WeiXinGongZhongHaoPa2PageHandler),
    (r"/activity/(wxgzh[3|6])", channel.zonghe.WeiXinGongZhongHaoZongHe3PageHandler),
    (r"/activity/wxgzh4", channel.channel_no_idno.WeiXinGongZhongHaoPaDy4PageHandler),

    # 搜狗浏览器
    (r"/activity/(sgllq[1-2])", channel.pinzhong.SouGouLiuLanQiPaDyPageHandler),
    (r"/activity/(sgllq[3-6])", channel.zonghe.SouGouLiuLanQiZongHePageHandler),

    # 彩票活动
    (r"/activity/duibacpcpc1", channel.lottery.DuiBaCaiPiaoCPC1PageHandler),
    (r"/activity/duibacpcpc2", channel.lottery.DuiBaCaiPiaoCPC2PageHandler),
    (r"/activity/duibacpcpc3", channel.lottery.DuiBaCaiPiaoCPC3PageHandler),
    (r"/activity_mgb/tuiacpcpc1", channel.lottery.TuiaCaiPiao1PageHandler),
    (r"/activity_mgb/tuiacpcpc2", channel.lottery.TuiaCaiPiao2PageHandler),
    (r"/activity_mgb/tuiacpcpc3", channel.lottery.TuiaCaiPiao3PageHandler),
    (r"/activity/ywcp1", channel.lottery.YuWenCaiPiao1PageHandler),
    (r"/activity/ywcp2", channel.lottery.YuWenCaiPiao2PageHandler),
    (r"/activity/(heiniucp(?:[1-9]|10))", channel.lottery.HeiNiuCaiPiaoPageHandler),

    # 钱罐子
    (r"/activity/hnqgz", channel.qianguanzi.QianGuanZiPageHandler),

    # 百年新页面
    (r"/activity/hnbn", channel.bainian.HeiNiuBaiNianPageHandler),

    # 快递100
    (r"/activity/(kd[1-2])", channel.zonghe.KuaiDi100ZongHePageHandler),
    (r"/activity/(kd[3-4])", channel.e_bank.KuaiDi100EBankPageHandler),

    # 即富集团
    (r"/activity/(jfjt[1-2])", channel.zonghe.JiFuJiTuanZongHePageHandler),
    (r"/activity/(jfjt[3-4])", channel.e_bank.JiFuJiTuanEBankPageHandler),

    # 51福利
    (r"/activity/51ful", channel.qianfang.Ful51PaePageHandler),

    # 现金卡
    (r"/activity/hnxjk", channel.cash_card.CashCardPageHandler),

    # 手机管家
    (r"/activity/shoujgjzh", channel.e_bank.ShouJiGuanJiaEBankPageHandler),
    (r"/activity/shoujgjtks", channel.taikang.ShouJiGuanJIaTaiKangSPageHandler),
    (r"/activity/shoujgjpalt", channel.pingan.ShouJiGuanJiaPALTPageHandler),

    # 无线拓媒
    (r"/activity/wuxtmtksxk1", channel.taikang.WuXianTuoMeiShuxinkaSuperDesk),
    (r"/activity/wuxtmtkfcb1", channel.taikang.WuXianTuoMeiFeiChangBaoPageHander),
    (r"/activity/wuxtm3hy", channel.zonghe.WuXianTuoMei3HYPageHandler),
    (r"/activity/wuxtmwy", channel.duiba.WuXianTuoMeiWYPageHandler),
    (r"/activity/wuxtm3he1", channel.gooyo.WuXianTuoMei3He1PageHandler),

    # 平安wifi活动
    (r"/activity/pawifipa1", channel.duiba.PinganWiFiCpc1PageHandler),
    (r"/activity/pawifiofo3", channel.pingan_wifi.PingAnWifiOfo3PageHandler),
    (r"/activity/pawifmt1", channel.didi.PingAnWifiMTaiKangPageHandler),

    # 大都会新页面
    (r"/activity/hnddhnew", channel.daduhui.HeiNiuDaDuHuiPageHandler),

    # 艾睿万合
    (r"/activity/(wanhe[1-2])", channel.zonghe.AiRuiWanHeZhongHePageHandler),

    # 九天传媒
    (r"/activity/jiuttaik", channel.taikang.JiuTianChuanMeiFeiChangBaoPageHander),
    (r"/activity/jiuttzj", channel.didi.JiuTianChuanMeiZiJiaPageHandler),
    (r"/activity/jiuttwy", channel.duiba.JiuTianChuanMeiEBankPageHandler),

    # wxzf
    (r"/activity/(zfwzl(?:1|3))", channel.zonghe.ZFWZLZhongHePageHandler),
    (r"/activity/zfwzl2", channel.e_bank.ZFWZLEbankPageHandler),

    # 天脉摇一摇
    (r"/activity/(tvbeijing|tvshanghai|tvneimenggu|tvhebei|tvanhui|tvhenan|tvhubei|tvshanxi|tvshandong|tvjilin|tvheilongjiang|tvguangdong|tvliaoning|tvhunan|tvzhejiang)", channel.tv_yaoyiyao.TianMaiTVZongHePageHandler),

    # 券小美
    (r"/activity/qxm1", channel.zonghe.QuanXiaoMeiZongHePageHandler),
    (r"/activity/qxm2", channel.e_bank.QuanXiaoMeiEBankPageHandler),

    # 天云摇一摇
    (r"/activity/(tytvdd[1-4])", channel.tv_yaoyiyao.TianYunTvYaoYiYaoDiDiPageHandler),

    # 一点资讯
    (r"/activity/(yddy[1-2])", channel.pinzhong.YiDianZiXunPaDyPageHandler),
    (r"/activity/(ydqm[1-2])", channel.zonghe.YiDianZiXunZongHePageHandler),

    # 平安车主信用卡
    (r"/activity/hnpaczxyk1", channel.pingan.PinganCheZhuXinYongKa1PageHandler),
    (r"/activity/hnpaczxyk2", channel.pingan.PinganCheZhuXinYongKa2PageHandler),

    # 车行易
    (r"/activity/chexy3hy", channel.zonghe.CheXingYiZhongHePageHandler),
    # 车主宝典
    (r"/activity/chezbd3hy1", channel.zonghe.CheZhuBaoDianZhongHePageHandler),

    # 赢纳科技
    (r"/activity/ynkjdd1", channel.duiba.YingNaKeJiDiDiPageHandler),
    (r"/activity/ynkjzh1", channel.weiche.YingNaKeJiZhongHePageHandler),

    # 高铁
    (r"/activity/(gaotie[1-2])", channel.duiba.GaoTie1PageHandler),
    (r"/activity/(gaotie[3-4])", channel.taikang.GaoTie3FeiChangBaoPageHander),

    # 众智嘉能
    (r"/activity/zzjnzh1", channel.weiche.ZhongZhiJiaNengZongHe1PageHandler),

    # 短信渠道
    (r"/activity/bdxzh1", channel.weiche.BDuanXinZongHe1PageHandler),
    # 短信平台
    (r"/activity/dxpa1", channel.pingan.DuanXinPingAnPageHandler),
    (r"/activity/dxzh1", channel.weiche.DuanXinZongHePageHandler),

    # 谷友你我金融
    (r"/activity/(gyniwjr[1-2])", channel.pingan.GuYouNiWoJinRong1PageHandler),

    # 微梦想
    (r"/activity/wmxpa1", channel.pingan.WeiMengXiangPingAn1PageHandler),
    (r"/activity/wmxzh1", channel.guahao114.WeiMengXiangZongHe1PageHandler),
    # 途牛扫码
    (r"/activity/tun3h1", channel.guahao114.TuNiuSanHe1PageHandler),

    # 谷友掌上公交
    (r"/activity/(gyzhangsgj[1-2])", channel.taikang.GuYouZhangShangGongJiaoPageHander),
    # 谷友ofo
    (r"/activity/gyofo1", channel.pingan_wifi.GuYouOfoPageHandler),
    # 谷友电商
    (r"/activity/gymakwy", channel.qianfang.GuYouMAKWYPageHandler),

    # 智易
    (r"/activity/zhiyidd1", channel.duiba.ZhiYiDiDi1PageHandler),
    (r"/activity/zhiyizh1", channel.weiche.ZhiYiZongHe1PageHandler),
    # 晴空科技
    (r"/activity/gcwzh1", channel.weiche.QingKongKeJiZongHePageHandler),

    # 马立广告
    (r"/activity/maliggzh1", channel.weiche.MaLiGuangGaoZhongHe1PageHandler),

    # 禾连WiFi
    (r"/activity/hlwifizh1", channel.weiche.HeLianWifiZongHe1PageHandler),
    (r"/activity/hlwifidd1", channel.duiba.YingNaKeJiDiDiPageHandler),

    # 贷款推广活动
    (r"/activity/hndaikuan1", channel.daikuan.DaiKuanPageHandler),
    (r"/activity/hndaikuan2", channel.daikuan.TuiADaiKuanPageHandler_MGB),
    (r"/activity_mgb/(tuiadaikuan[1-5])", channel.daikuan.TuiADaiKuanPageHandler_MGB),
    (r"/activity/get_insurance_interface", channel.daikuan.GetInsuranceInterface),
    (r"/activity/get_captcha_interface", channel.daikuan.GetCaptchaInterface),
    # 一只大鱼贷款
    (r"/activity/yzdydk1", channel.daikuan.YiZhiDaYuDaiKuanPageHandler),
    # 乐惠贷款
    (r"/activity/lehuidk1", channel.daikuan.LeHuiDaiKuanPageHandler),
    (r"/activity/lhdkcpc1", channel.daikuan.LeHuiDaiKuanCPCPageHandler),
    (r"/activity/lhddcpc1", channel.duiba.LeHuiDiDiCPCPageHandler),
    (r"/activity/lhmtcpc1", channel.didi.LeHuiMeiTuanCPC1TaiKangPageHandler),
    # 享多多贷款
    (r"/activity/xiangduoduodk1", channel.daikuan.XiangDuoDuoDaiKuanPageHandler),
    # 享多多
    (r"/activity/xiangddmt1", channel.didi.XiangDuoDuoMeiTuanPageHandler),

    # Tedm贷款
    (r"/activity/Tedmdk1", channel.daikuan.TEDMDaiKuanPageHandler),
    # 行者
    (r"/activity/xingzhedk1", channel.daikuan.XingZheDaiKuanPageHandler),
    # 新头条
    (r"/activity/newjrtt1", channel.daikuan.NewJinRiTouTiaoDaiKuanPageHandler),
    (r"/activity/newjrttzx", channel.tv_yaoyiyao.NewJinRiTouTiaoZengXianPageHandler),
    # 世涛
    (r"/activity/shitaodk1", channel.daikuan.ShiTaoDaiKuanPageHandler),
    # 黑牛平安
    (r"/activity/(hndaikuanPA[1-5])", channel.daikuan.HeiNiuDaiKuanPAPageHandler),


    # 新版黑牛有钱
    (r"/activity/heiniuyouqian1", channel.daikuan.HeiNiuYouQianPageHandler),
    (r"/activity/get_hnyq_captcha", channel.daikuan.GetHeiNiuYouQianCaptchaInterface),
    
     # 黑牛有钱V3.0增加延迟承保功能
    (r"/activity/heiniuyouqian3", channel.daikuan3.HeiNiuYouQianIndexPageHandler),
    (r"/activity/checkuser3", channel.daikuan3.HeiNiuYouQianCheckUserStatusPageHandler),
    (r"/activity/verifycode3", channel.daikuan3.HeiNiuYouQianVeryCodePageHandler),
    (r"/activity/hnyouqianinfo3", channel.daikuan3.HeiNiuYouQianInfoPageHandler),
    (r"/activity/hnyouqianend3", channel.daikuan3.HeiNiuYouQianRecommendPageHandler),
    (r"/activity/hnyouqianclick3", channel.daikuan3.HeiNiuYouQianClickPageHandler),
    (r"/activity/hnyouqiancron3", channel.daikuan3.HeiNiuYouQianCronPageHandler),
    
    #阳光贷款页面做展示用
    (r"/activity/ygdaikuan1", channel.daikuan.YangGuangDaiKuanPageHandler),

    # 一只大鱼
    (r"/activity/yzdyofo1", channel.pingan_wifi.YiZhiDaYuOfoPageHandler),
    (r"/activity/yzdyzh1", channel.weiche.YiZhiDaYuZongHe1PageHandler),
    (r"/activity/yzdydd1", channel.duiba.YiZhiDaYuDiDiPageHandler),

    # 谷友酷骑单车
    (r"/activity/gykuqdc1", channel.pingan_wifi.GuYouKuQiDanChe1PageHandler),

    # 录屏大师
    (r"/activity/lupdsofo", channel.pingan_wifi.LuPingDaShiPageHandler),

    # 互动推滴滴
    (r"/activity/hudongtcpc", channel.duiba.HuDongTuiCPCPageHandler),
    # 91投
    (r"/activity/91tou3h1", channel.guahao114.New91Tou3He1PageHandler),
    # 永安行
    (r"/activity/gyyongax1", channel.pingan_wifi.GuYouYongAnXing1PageHandler),
    # 光微科技
    (r"/activity/gwkjofo1", channel.pingan_wifi.GuangWeiKeJiOfoPageHandler),
    (r"/activity/gwkjzh1", channel.weiche.GuangWeiKeJiZongHe1PageHandler),
    (r"/activity/gwkjdd1", channel.duiba.GuangWeiKeJiDiDiPageHandler),
    # 加多宝
    (r"/activity/jdbtk1", channel.taikang.JiaDuoBaoTaiKangPageHander),
    # 万合新福利社
    (r"/activity/wanhtk1", channel.taikang.WanHeTaiKangPageHander),
    # 广州骏伯
    (r"/activity/gzjunbtk1", channel.taikang.GuangZhouJunBoTaiKangPageHander),
    # 海保
    (r"/activity/haibtk1", channel.taikang.HaiBaoTaiKangPageHander),
    # 往返APP
    (r"/activity/wftk1", channel.taikang.WangFanAPPTaiKangPageHander),
    # 天翼视讯
    (r"/activity/tysxtk1", channel.taikang.TianYiShiXunTaiKangPageHander),
    # 趣呀app
    (r"/activity/quya3he1", channel.gooyo.QuYa3He1PageHandler),
    # 去哪儿
    (r"/activity/(taikang_quner100[1-9]|taikang_quner200[1-9])", channel.taikang.TaiKangQuner20PageHander),
    (r"/activity/(taikang_quner[12]010)", channel.taikang.TaiKangQuner20PageHander),
    # 智慧推
    (r"/activity/(taikang_txzht[1-5])", channel.taikang.TaiKangZhiHuiTuiPageHander),
    # 智能短信
    (r"/activity/zndx1", channel.taikang.ZhiNengDuanXinPage1Hander),
    (r"/activity/zndx2", channel.taikang.ZhiNengDuanXinPage2Hander),
    # 东鹏特饮
    (r"/activity/dongptypayd1", channel.pingan.DongPengTeYinPingAnYunDongPageHandler),
    (r"/activity/dongpcx", channel.taikang.DongPengCXPageHander),
    (r"/activity/dptkcx", channel.taikang.DongPengCXPageHander),
    # 第五金融
    (r"/activity/(diwujrtk[1-2])", channel.taikang.DiWuJinRongChuXingPageHander),
    # 爱财贷
    (r"/activity/aicaidtk1", channel.taikang.AiCaiDaiChuXingPageHander),
    # 约单泰康
    (r"/activity/yuedtk1", channel.taikang.YueDanTaiKangPageHander),
    # 大燕网
    (r"/activity/daywtk1", channel.taikang.DaYanWangChuXingPageHander),

    # 平安上海组合
    (r"/activity/pash1", channel.zonghe.PingAnShangHaiZuHe1PageHandler),
    # 返利网
    (r"/activity/fanlwtk1", channel.taikang.FanLiWangTaiKangPageHander),
    # 万合优拜单车
    (r"/activity/wanhyoub1", channel.pingan_wifi.WanHeYouBaiDanChePageHandler),
    # 万合酷骑单车
    (r"/activity/wanhkqgq1", channel.taikang.WanHeKuQiDanCheGuoQingPageHander),
    # 乐投壹佰
    (r"/activity/letou1001", channel.taikang.LeTouYiBaiChuXingPageHander),

    # 豆盟广告
    (r"/activity/doumtk1", channel.taikang.DouMengChuXingPageHander),
    (r"/activity/doumdd1", channel.duiba.DouMengDiDiPageHandler),
    (r"/activity/doummt1", channel.didi.DouMengMeiTuanTaiKangPageHandler),

    # 地推团队
    (r"/activity/(dituitk[1-3])", channel.taikang.DiTuiTaiKangPageHander),

    # 好车主
    (r"/activity/haochezhu1", channel.zonghe.HaoCheZhuZongHePageHandler),
    (r"/activity/haochezhu2", channel.pinzhong.HaoCheZhuPaPageHandler),
    (r"/activity/haochezhu3", channel.duiba.HaoCheZhuEBankPageHandler),

    # 盒子支付
    (r"/activity/hezzf3h1", channel.guahao114.HeZiZhiFuZongHe1PageHandler),

    # 收钱吧
    (r"/activity/(shouqbgq[1-3])", channel.taikang.ShouQianBaGuoQingPageHander),

    # 窝窝支付
    (r"/activity/wowzfxinj1", channel.taikang.WoWoZhiFuHuanKuanJinPageHander),
    (r"/activity/wowzfmt1", channel.didi.WoWoZhiFuMeiTuanPageHandler),
    (r"/activity/go_wowo_heika", channel.redirect.GoToWoWoHeiKaPageHandler),
    (r"/activity/wowzfcpczfb1", channel.didi.WoWoZhiFuCPCZhiFuBaoPageHandler),
    (r"/activity/wowzfcpcdd1", channel.duiba.WoWoZhiFuDiDiCPCPageHandler),
    (r"/activity/wowdk1", channel.daikuan.WoWoZhiFuDaiKuanPageHandler),
    # 考拉先生
    (r"/activity/kaolcpcmt1", channel.didi.KaoLaXianShengMeiTuanPageHandler),

    # 美团
    (r"/activity/meitwm1", channel.didi.MeiTuanPageHandler),
    (r"/activity/meitwm3", channel.didi.MeiTuan3PageHandler),
    # 给美团看的
    (r"/activity/meitwm2", channel.didi.MeiTuan2PageHandler),

    # 推广转盘赠险
    (r"/activity/hnzonghe1", channel.zonghe.IPPanDingZongHePageHandler),

    # 黑牛展示页面
    (r"/activity/huaxiazh1", channel.zonghe.HuaXiaZongHePageHandler),
    (r"/activity/huaxiaddcpc1", channel.duiba.HuaXiaDiDiCPCPageHandler),
    (r"/activity/huaxiacpc1", channel.duiba.HuaXiaNewNoDiDiPageHandler),
    (r"/activity/taipingddcpc1", channel.duiba.TaiPingDiDiCPCPageHandler),
    (r"/activity/taipingcpc1", channel.duiba.TaiPingNoDiDiPageHandler),
    (r"/activity/hnzgrs1", channel.duiba.ZhongGuoRenShouBPageHandler),

    # 信用卡还款金活动
    (r"/activity/xykhkj1", channel.taikang.XinYongKaHuanKuanJinPageHander),
    (r"/activity/check_limit", channel.taikang.CheckLimitInterface),

    # 自动生成渠道
    (r"/activities/(.*)", channel.activities_handler.ActivitiesHandler),
    (r"/new_activity", channel.activities_handler.NewChannelHandler),
    (r"/activity_pages", channel.activities_handler.ListActivitiesHandler),

    (r"/sms/chuanglan/callback", insurance.callback.chuanglan.ChuanglanReceive),
    # (r"/reserve", channel.ReserveHandler),
    (r"/api/v1/bjlt/stat", insurance.out_api.bjlt.views.BeiJingLianTongStatHandler),
    (r"/api/v1/bjlt/search", insurance.out_api.bjlt.views.BeiJingLianTongSearchHandler),
    (r"/api/v1/bjlt/index", insurance.out_api.bjlt.views.BeiJingLianTongIndexHandler),
    (r"/api/v1/zhihuidaoyou/index", insurance.out_api.quner.views.ZhiHuiQuNerIndexHandler),
    (r"/api/v1/zhihuidaoyou/overview", insurance.out_api.quner.views.ZhiHuiQuNerOverviewHandler),
    (r"/api/traffic_stat", insurance.out_api.market_stat.views.MarketStatBaseHandler),
    (r"/api/partner_stat", insurance.out_api.partner_stat.views.PartnerStatBaseHandler),
    (r"/api/current_stat", insurance.out_api.partner_stat.current.CurrentStatBaseHandler),
    (r"/api/partner_extend_stat", insurance.out_api.partner_stat.views.PartnerStatExtendHandler),
    (r"/api/partner_extend_stat2", insurance.out_api.partner_stat.views.PartnerStatExtend2Handler),
    (r"/api/partner_current_stat", insurance.out_api.partner_stat.views.PartnerStatCurrentHandler),
    (r"/api/real_time_stat", insurance.out_api.real_time_stat.views.RealTimeStatCurrentHandler),
    (r"/api/hnyq_stat", insurance.out_api.market_stat.current.HeiNiuYouQianInsuranceHandler),
    (r"/api/loan/baixing/mobile", insurance.out_api.baixing.views.BaixingMobileFetcherHandler),
    (r"/api/loan/baixing/confirmation", insurance.out_api.baixing.views.BaixingConfirmationHandler),
    (r"/api/local/policy_checker", insurance.local_api.policy_checker.views.PolicyCheckerPageHandler),
    (r"/api/local/pa_policy_checker", insurance.local_api.pingan_policy_parser.views.PinganPolicyParserHandler),
    (r"/api/local/all_policy_checker", insurance.local_api.pingan_policy_parser.views.AllPolicyParserHandler),
    (r"/api/local/gen/phone_token", insurance.local_api.pingan_policy_parser.views.GenPhoneTokenHandler),
    (r"/api/local/captcha/info", insurance.local_api.show_captcha.views.CaptchaLocalShowerPageHandler),

    # 外部链接重定向
    (r"/redirect/didi", channel.redirect.DiDiRedirectPageHandler),
    (r"/redirect/jinbi4", channel.redirect.GoToJinBi4PageHandler),


    # ----------------------------------------------  福利社相关  --------------------------------------------------


    (r"/activity/no_redirect1", channel.redirect.NoRedirectPageHandler),
    (r"/activity/dd_redirect1", channel.redirect.DiDiRedirectPageHandler),
    (r"/activity/dd_redirect_new1", channel.redirect.NewDiDiRedirectPageHandler),
    (r"/activity/mobai_redirect1", channel.redirect.MoBaiRedirectPageHandler),
    (r"/activity/cp_redirect1", channel.redirect.CaiPiaoRedirectPageHandler),
    (r"/activity/qgz_redirect1", channel.redirect.QianGuanZiRedirectPageHandler),
    (r"/activity/mtwm_redirect1", channel.redirect.MeiTuanWaiMaiRedirectPageHandler),
    (r"/activity/51xyk_redirect1", channel.redirect.XinYongKa51RedirectPageHandler),
    (r"/activity/mtwm_redirect2", channel.redirect.MeiTuanWaiMaiRedirect2PageHandler),
    (r"/activity/51xyk_redirect2", channel.redirect.XinYongKa51Redirect2PageHandler),
    (r"/activity/no_redirect2", channel.redirect.NoRedirect2PageHandler),

    (r"/activity/trans_wangzherongyao1", channel.redirect.WangZheRongYaoTransPageHandler),
    (r"/activity/trans_quanmama1", channel.redirect.QuanMaMaTransPageHandler),
    (r"/activity/trans_dididalibao1", channel.redirect.DiDiLanJieDaLiBaoPageHandler),
    (r"/activity/trans_mtdalibao1", channel.redirect.MeiTuanDaLiBaoPageHandler),
    (r"/activity/trans_mtdalibao2", channel.redirect.MeiTuanDaLiBao2PageHandler),
    (r"/activity/trans_51xykdalibao1", channel.redirect.XinYongKa51DaLiBaoPageHandler),
    (r"/activity/trans_51xykdalibao2", channel.redirect.XinYongKa51DaLiBao2PageHandler),
    (r"/activity/trans_back_dalibao1", channel.redirect.BackDaLiBaoPageHandler),
    (r"/activity/trans_back_dalibao2", channel.redirect.BackDaLiBao2PageHandler),

    (r"/activity/tiantianaicaipiao_trans1", channel.redirect.TianTianAiCaiPiaoTransPageHandler),
    (r"/activity/tiantianaicaipiao_trans2", channel.redirect.TianTianAiCaiPiaoTransLJPageHandler),
    (r"/activity/tiantianaicaipiao_trans4", channel.redirect.TianTianAiCaiPiaoTransHTLJPageHandler),
    (r"/activity/tiantianaicaipiao_bxm_trans1", channel.redirect.TianTianAiCaiPiaoTransBXMPageHandler),

    (r"/activity/kuaishoucaipiao_trans1", channel.redirect.KuaiShouCaiPiaoTransPageHandler),
    (r"/activity/kuaishoucaipiao_trans2", channel.redirect.KuaiShouCaiPiaoTrans2PageHandler),

    (r"/activity/download_trans", channel.redirect.DownloadTransPageHandler),
    (r"/activity/download_trans_rrzcp", channel.redirect.RenRenZhongCaiPiaoDownloadTransPageHandler),

    (r"/activity/gojinbi4", channel.redirect.GoToJinBi4PageHandler),
    (r"/activity/godidi1", channel.redirect.GoToDiDiPageHandler),
    (r"/activity/goofo1", channel.redirect.GoToOfoPageHandler),
    (r"/activity/gojkw1", channel.redirect.GoToJieKuanWangPageHandler),
    (r"/activity/gowc1", channel.redirect.GoToWaCaiPageHandler),
    (r"/activity/gojdjk1", channel.redirect.GoToJianDanJieKuanPageHandler),
    (r"/activity/gojdjk_new1", channel.redirect.GoToJianDanJieKuanNewPageHandler),
    (r"/activity/cpdownload1", channel.redirect.CaiPiaoDownloadPageHandler),
    (r"/activity/cpdownload2", channel.redirect.CaiPiaoDownload2PageHandler),
    (r"/activity/cpdownload3", channel.redirect.CaiPiaoDownload3PageHandler),
    (r"/activity/cpdownload_bxm", channel.redirect.BXMCaiPiaoDownloadPageHandler),
    (r"/activity/cpdownloadiphone1", channel.redirect.CaiPiaoDownloadIphonePageHandler),
    (r"/activity/cpdownloadandroid1", channel.redirect.CaiPiaoDownloadAndroidPageHandler),
    (r"/activity/cpdownloadandroid_wx", channel.redirect.CaiPiaoDownloadAndroidPageHandler),
    (r"/activity/cpdownloadiphone2", channel.redirect.CaiPiaoDownloadIphone2PageHandler),
    (r"/activity/cpdownloadandroid2", channel.redirect.CaiPiaoDownloadAndroid2PageHandler),
    (r"/activity/cpdownloadiphone3", channel.redirect.CaiPiaoDownloadIphone3PageHandler),
    (r"/activity/cpdownloadandroid3", channel.redirect.CaiPiaoDownloadAndroid3PageHandler),
    (r"/activity/cpdownloadandroid_bxm", channel.redirect.BXMCaiPiaoDownloadAndroidPageHandler),
    (r"/activity/gopaph1", channel.redirect.GoToPingAnPuHuiPageHandler),
    (r"/activity/gopaph2", channel.redirect.GoToPingAnPuHui2PageHandler),
    (r"/activity/goheika1", channel.redirect.GoToHeikaPageHandler),
    (r"/activity/goheika2", channel.redirect.GoToHeika2PageHandler),
    (r"/activity/goheika3", channel.redirect.GoToHeika3PageHandler),
    (r"/activity/goheika4", channel.redirect.GoToHeika4PageHandler),
    (r"/activity/goheika5", channel.redirect.GoToHeika5PageHandler),
    (r"/activity/goheika6", channel.redirect.GoToHeika6PageHandler),
    (r"/activity/goheika7", channel.redirect.GoToHeika7PageHandler),
    (r"/activity/goheika_wowo1", channel.redirect.GoToHeikaWoWoPageHandler),
    (r"/activity/goheika_51flw1", channel.redirect.GoToWoWoHeiKaPageHandler),
    (r"/activity/go_heika_CPA1", channel.redirect.GoToHeikaCPAPageHandler),
    (r"/activity/gosudaizhijia1", channel.redirect.GoToSuDaiZhiJiaPageHandler),
    (r"/activity/goqianguanzi1", channel.redirect.GoToQianGuanZiPageHandler),
    (r"/activity/goqianguanzi2", channel.redirect.GoToQianGuanZiPageHandler),
    (r"/activity/goqianguanzi_wowo1", channel.redirect.GoToQianGuanZiPageHandler),
    (r"/activity/goqianguanzi1_zx", channel.redirect.GoToQianGuanZiZengXianPageHandler),
    (r"/activity/gosudaizhijia1_zx", channel.redirect.GoToSuDaiZhiJiaPageHandler),
    (r"/activity/gopinganwacai1_zx", channel.redirect.GoToPingAnWaCaiPageHandler),
    (r"/activity/gopinganpuhui1_zx", channel.redirect.GoToPAPuHuiDaiKuanWangPageHandler),
    (r"/activity/gojiekuanzhuangjia1_zx", channel.redirect.GoToJieKuanZhuangJiaPageHandler),
    (r"/activity/go2345daikuanwang1_zx", channel.redirect.GoTo2345DaiKuanWangPageHandler),
    (r"/activity/goxianjinka_zx", channel.redirect.GoToXianJinKaPageHandler),
    (r"/activity/goleshua1", channel.redirect.GoToLeShuaPageHandler),
    (r"/activity/goleshua_zp", channel.redirect.GoToLeShuaZhuanPanPageHandler),
    (r"/activity/go_jiaotongka1", channel.redirect.GoToJiaoTongCreditPageHandler),
    (r"/activity/go_zhongxinka1", channel.redirect.GoToZhongXinCreditPageHandler),
    (r"/activity/go_zhongxinka2", channel.redirect.GoToZhongXinCredit2PageHandler),
    (r"/activity/go_zhaoshangka1", channel.redirect.GoToZhaoShangCreditPageHandler),
    (r"/activity/go_pufaka1", channel.redirect.GoToPuFaCreditPageHandler),
    (r"/activity/go_uinpay_index1", channel.redirect.GoToEntranceCreditPageHandler),
    (r"/activity/go_mojie1", channel.redirect.GoToMoJiePageHandler),
    (r"/activity/go_caipiao_zx", channel.redirect.GoToCaiPiaoPageHandler),
    (r"/activity/go_paxyk_yd", channel.redirect.GoToPingAnXinYongKaYDPageHandler),
    (r"/activity/go_paxyk_pc", channel.redirect.GoToPingAnXinYongKaPCPageHandler),
    (r"/activity/go_zhaoshangka2", channel.redirect.GoToZhaoShangCredit2PageHandler),
    (r"/activity/go_minshengka1", channel.redirect.GoToMinShengCreditPageHandler),
    (r"/activity/go_minshengka2", channel.redirect.GoToMinShengCredit2PageHandler),
    (r"/activity/go_guangfaka1", channel.redirect.GoToGuangFaCreditPageHandler),
    (r"/activity/go_liminwang1", channel.redirect.GoToLiMinWangPageHandler),
    (r"/activity/go_liminwang2", channel.redirect.GoToLiMinWang2PageHandler),
    (r"/activity/go_xyqb1", channel.redirect.GoToXinYongQianBaoPageHandler),
    (r"/activity/go_xianjinka1", channel.redirect.GoToXianJinKa2PageHandler),
    (r"/activity/go_wolaidai1", channel.redirect.GoToWoLaiDaiPageHandler),
    (r"/activity/go_yiyuanduobao_ios1", channel.redirect.GoToYiYuanDuoBaoIosPageHandler),
    (r"/activity/go_yiyuanduobao_android1", channel.redirect.GoToYiYuanDuoBaoAndroidPageHandler),
    (r"/activity/go_jiedianqian1", channel.redirect.GoToJieDianQianPageHandler),
    (r"/activity/go_jiedianqian2", channel.redirect.GoToJieDianQian2PageHandler),
    (r"/activity/go_jiedianqian3", channel.redirect.GoToJieDianQian3PageHandler),
    (r"/activity/go_jiedianqian_ht2", channel.redirect.GoToJieDianQianHT2PageHandler),
    (r"/activity/go_xingxingqiandai1", channel.redirect.GoToXingXingQianDaiPageHandler),
    (r"/activity/go_vipkid1", channel.redirect.GoToVipKidPageHandler),
    (r"/activity/go_vipkid1_1", channel.redirect.GoToVipKid1_1PageHandler),
    (r"/activity/go_vipkid1_2", channel.redirect.GoToVipKid1_2PageHandler),
    (r"/activity/go_vipkid1_3", channel.redirect.GoToVipKid1_3PageHandler),
    (r"/activity/go_huanleduobao_android1", channel.redirect.GoToHuanLeDuoBaoAndroidPageHandler),
    (r"/activity/go_huanleduobao_ios1", channel.redirect.GoToHuanLeDuoBaoIOSPageHandler),
    (r"/activity/go_mobai1", channel.redirect.GoToMoBaiPageHandler),
    (r"/activity/go_guangdaka1", channel.redirect.GoToGuangDaKaPageHandler),
    (r"/activity/go_luolizhajinhua1", channel.redirect.GoToLuoLiZhaJinHuaPageHandler),
    (r"/activity/go_quanmama1", channel.redirect.GoToQuanMaMaPageHandler),
    (r"/activity/go_quanmama2", channel.redirect.GoToQuanMaMa2PageHandler),
    (r"/activity/go_yirendai1", channel.redirect.GoToYiRenDaiPageHandler),
    (r"/activity/go_dazhongdianping1", channel.redirect.GoToDaZhongDianPingPageHandler),
    (r"/activity/go_laicaicaipiao1", channel.redirect.GoToLaiCaiCaiPiaoPageHandler),
    (r"/activity/go_xianjinxia1", channel.redirect.GoToXianJinXiaPageHandler),
    (r"/activity/go_jinbeiqipai_android1", channel.redirect.GoToJinBeiQiPaiAndroidPageHandler),
    (r"/activity/go_jinbeiqipai_ios1", channel.redirect.GoToJinBeiQiPaiIOSPageHandler),
    (r"/activity/go_wanhaocaipiao1", channel.redirect.GoToWanHaoCaiPiaoPageHandler),
    (r"/activity/go_wanhaocaipiao2", channel.redirect.GoToWanHaoCaiPiao2PageHandler),
    (r"/activity/go_baoxinishoubiao1", channel.redirect.GoToBaoXiNiShouBiaoPageHandler),
    (r"/activity/go_yinhezhixing1", channel.redirect.GoToYinHeZhiXingPageHandler),
    (r"/activity/go_fopaiheiyaoshi1", channel.redirect.GoToFoPaiHeiYaoShiPageHandler),
    (r"/activity/go_pixiu1", channel.redirect.GoToPiXiuPageHandler),
    (r"/activity/go_yicaidao1", channel.redirect.GoToYiCaiDaoPageHandler),
    (r"/activity/go_yicaidao_gxcdb1", channel.redirect.GoToGongXiangChongDianBaoYiCaiDaoPageHandler),
    (r"/activity/go_paczxyk1", channel.redirect.GoToPingAnXinYongKaYDPageHandler),
    (r"/activity/go_buyudashi1", channel.redirect.GoToBuYuDaShiPageHandler),
    (r"/activity/go_koudaiauction_ios1", channel.redirect.GoToKouDaiAuctionIOSPageHandler),
    (r"/activity/go_koudaiauction_android1", channel.redirect.GoToKouDaiAuctionAndroidPageHandler),
    (r"/activity/go_huaerjie1", channel.redirect.GoToHuaErJiePageHandler),
    (r"/activity/go_jinronghui1", channel.redirect.GoToJinRongHuiPageHandler),
    (r"/activity/go_heiniudaikuan1", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/go_heiniudaikuan2", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/go_heiniudaikuan3", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/go_heiniudaikuan4", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/go_heiniudaikuan_lunbo", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/go_heiniudaikuan_wowo", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/go_jinshancaipiao1", channel.redirect.GoToJinShanCaiPiaoPageHandler),
    (r"/activity/go_kuaiyihua1", channel.redirect.GoToKuaiYiHuaPageHandler),
    (r"/activity/go_taoxinwen1", channel.redirect.GoToTaoXinWenPageHandler),
    (r"/activity/go_quanminduobao_ios1", channel.redirect.GoToQuanMingDuoBaoIOSPageHandler),
    (r"/activity/go_quanminduobao_android1", channel.redirect.GoToQuanMingDuoBaoAndroidPageHandler),
    (r"/activity/go_qiuqiudoudizhu1", channel.redirect.GoToQiuQiuDouDiZhuPageHandler),
    (r"/activity/go_kuhuasuoping1", channel.redirect.GoToKuHuaSuoPingPageHandler),
    (r"/activity/go_shanghaiyhxyk1", channel.redirect.GoToShangHaiYinHangXinYongKaPageHandler),
    (r"/activity/go_leshua2", channel.redirect.GoToLeShua2PageHandler),
    (r"/activity/go_leshua_out", channel.redirect.GoToLeShuaOutPageHandler),
    (r"/activity/go_qianyoulu1", channel.redirect.GoToQianYouLuPageHandler),
    (r"/activity/go_hulishajin1", channel.redirect.GoToHuLiShaJinPageHandler),
    (r"/activity/go_heiyaoshi_pixiu1", channel.redirect.GoToHeiYaoShiPiXiuPageHandler),
    (r"/activity/go_wonenglicai1", channel.redirect.GoToWoNengLiCaiPageHandler),
    (r"/activity/go_heiniubaoxian1", channel.redirect.GoToHeiNiuBaoXianPageHandler),
    (r"/activity/go_shandai1", channel.redirect.GoToShanDaiPageHandler),
    (r"/activity/go_bingsineiku1", channel.redirect.GoToBingSiNeiKuPageHandler),
    (r"/activity/go_T_shirtman1", channel.redirect.GoToTShirtManPageHandler),
    (r"/activity/go_hengxinmetal1", channel.redirect.GoToHengXinMetalPageHandler),
    (r"/activity/go_quanminauction_android1", channel.redirect.GoToQuanMinAuctionPageHandler),
    (r"/activity/go_quanminauction_ios1", channel.redirect.GoToQuanMinAuctionPageHandler),
    (r"/activity/go_koudaijc_ios1", channel.redirect.GoToKouDaiJingCaiIOSPageHandler),
    (r"/activity/go_koudaijc_android1", channel.redirect.GoToKouDaiJingCaiAndroidPageHandler),
    (r"/activity/go_wanrendoudizhu1", channel.redirect.GoToWanRenDouDiZhuPageHandler),
    (r"/activity/go_wanrendoudizhu2", channel.redirect.GoToWanRenDouDiZhu2PageHandler),
    (r"/activity/go_wanrendoudizhu_zp", channel.redirect.GoToWanRenDouDiZhuZPPageHandler),
    (r"/activity/go_daishangqian1", channel.redirect.GoToDaiShangQianPageHandler),
    (r"/activity/go_yiyuanduobao2_android", channel.redirect.GoToXYDuoBao2AndroidPageHandler),
    (r"/activity/go_hengxinmetal1_zp", channel.redirect.GoToHengXingMetalZP1PageHandler),
    (r"/activity/go_wangzherongyao1", channel.redirect.GoToWangZheRongYaoKaPageHandler),
    (r"/activity/go_baoxiniqinglvbiao1", channel.redirect.GoToBaoXiNiQingLvBiaoPageHandler),
    (r"/activity/go_tiantianzhajinhua1", channel.redirect.GoToTianTianZhaJinHuaPageHandler),
    (r"/activity/go_tengxunlicaitong1", channel.redirect.GoToTengXunLiCaiTongPageHandler),
    (r"/activity/go_xiangqiandai1", channel.redirect.GoToXiangQianDaiPageHandler),
    (r"/activity/go_baidujinrong1", channel.redirect.GoToBaiDuJinRongPageHandler),
    (r"/activity/go_360jietiao1", channel.redirect.GoTo360JieTiaoPageHandler),
    (r"/activity/go_360jietiao_gxcdb1", channel.redirect.GoToGongXiangChongDianBao360JieTiaoPageHandler),
    (r"/activity/go_yongqianbao1", channel.redirect.GoToYongQianBaoPageHandler),
    (r"/activity/go_lvshoujianfei1", channel.redirect.GoToLvShouJianFeiPageHandler),
    (r"/activity/go_binzhiheika1", channel.redirect.GoToBinZhiHeiKaPageHandler),
    (r"/activity/go_dianwanchengzhajinhua1", channel.redirect.GoToDianWanChengZhaJinHuaPageHandler),
    (r"/activity/go_songjiangdai1", channel.redirect.GoToSongJiangDaiPageHandler),
    (r"/activity/go_kaixinqianbao1", channel.redirect.GoToKaiXinQianBaoPageHandler),
    (r"/activity/go_kaniu1", channel.redirect.GoToKaNiuPageHandler),
    (r"/activity/go_jiekuanzhuanjia1", channel.redirect.GoToJieKuanZhuanJiaPageHandler),
    (r"/activity/go_yinghuangyule1", channel.redirect.GoToYingHuangYuLePageHandler),
    (r"/activity/go_360daikuan1", channel.redirect.GoTo360DaiKuanPageHandler),
    (r"/activity/go_51xinyongkaguanjia1", channel.redirect.GoTo51XinYongKaGuanJiaPageHandler),
    (r"/activity/go_51xinyongkaguanjia2", channel.redirect.GoTo51XinYongKaGuanJia2PageHandler),
    (r"/activity/go_51xinyongkaguanjia3", channel.redirect.GoTo51XinYongKaGuanJia3PageHandler),
    (r"/activity/go_51xinyongkaguanjia_wowo1", channel.redirect.GoTo51XinYongKaGuanJiaWoWoPageHandler),
    (r"/activity/go_niwodai1", channel.redirect.GoToNiWoDaiPageHandler),
    (r"/activity/go_xianjindai1", channel.redirect.GoToXianJinDaiPageHandler),
    (r"/activity/go_rong360_1", channel.redirect.GoToRong360PageHandler),
    (r"/activity/go_rong360_zp", channel.redirect.GoToRong360ZPPageHandler),
    (r"/activity/go_rong360_lunbo", channel.redirect.GoToRong360LunBoPageHandler),
    (r"/activity/go_leshua3", channel.redirect.GoToLeShua3PageHandler),
    (r"/activity/go_leshua_zp3", channel.redirect.GoToLeShuaZP3PageHandler),
    (r"/activity/go_leshua_xq_zp3", channel.redirect.GoToLeShuaXiangQianZP3PageHandler),
    (r"/activity/go_leshua_zp", channel.redirect.GoToLeShuaZPPageHandler),
    (r"/activity/go_leshua_ht4", channel.redirect.GoToLeShuaHT4PageHandler),
    (r"/activity/go_shandianpaimai1", channel.redirect.GoToShanDianPaiMaiPageHandler),
    (r"/activity/go_wangyiguijinshu1", channel.redirect.GoToWangYiGuiJinShuPageHandler),
    (r"/activity/go_mojie2", channel.redirect.GoToMoJie2PageHandler),
    (r"/activity/go_xinerfu1", channel.redirect.GoToXinErFuPageHandler),
    (r"/activity/go_tongchengyeyou1", channel.redirect.GoToTongChengYeYouPageHandler),
    (r"/activity/go_360daikuan2", channel.redirect.GoTo360DaiKuan2PageHandler),
    (r"/activity/go_fanliwang1", channel.redirect.GoToFanLiWangPageHandler),
    (r"/activity/go_bxmzpzh1", channel.redirect.GoToBXMZhuanPanZHPageHandler),
    (r"/activity/go_lanyueqipai1", channel.redirect.GoToLanYueQiPaiPageHandler),
    (r"/activity/go_weijiaoyi1", channel.redirect.GoToWeiJiaoYiPageHandler),
    (r"/activity/go_hnfopai1", channel.redirect.GoToHeiNiuFoPaiPageHandler),
    (r"/activity/go_hnfopai2", channel.redirect.GoToHeiNiuFoPai2PageHandler),
    (r"/activity/go_dingdangkuaiyao1", channel.redirect.GoToDingDangKuaiYaoPageHandler),
    (r"/activity/go_shandianjiangjia1", channel.redirect.GoToShanDianJiangJiaPageHandler),
    (r"/activity/go_boluodai1", channel.redirect.GoToJuJiuPeiPageHandler),
    (r"/activity/go_zhuanqian1", channel.redirect.GoToZhuanQianPageHandler),
    (r"/activity/go_daiba1", channel.redirect.GoToDaiBaPageHandler),
    (r"/activity/go_daiba_ht1", channel.redirect.GoToDaiBaHT1PageHandler),
    (r"/activity/go_dingguagua1", channel.redirect.GoToDingGuaGuaPageHandler),
    (r"/activity/go_tuhaodayingjia1", channel.redirect.GoToTuHaoDaYingJiaPageHandler),
    (r"/activity/go_xianjinjiekuan1", channel.redirect.GoToXianJinJieKuanPageHandler),
    (r"/activity/go_pengboyule1", channel.redirect.GoToPengBoYuLePageHandler),
    (r"/activity/go_zhaoshangka3", channel.redirect.GoToZhaoShangCredit3PageHandler),
    (r"/activity/go_tiantianaicaipiao1", channel.redirect.GoToTianTianAiCaiPiaoPageHandler),
    (r"/activity/go_tiantianaicaipiao_lj1", channel.redirect.GoToTianTianAiCaiPiaoLJPageHandler),
    (r"/activity/go_tiantianaicaipiao_wt1", channel.redirect.GoToTianTianAiCaiPiaoWTZPPageHandler),
    (r"/activity/go_tiantianaicaipiao_ht1", channel.redirect.GoToTianTianAiCaiPiaoHuiTuiPageHandler),
    (r"/activity/go_tiantianaicaipiao_ios1", channel.redirect.GoToTianTianAiCaiPiaoIOSPageHandler),
    (r"/activity/go_tiantianaicaipiao_ios_lj1", channel.redirect.GoToTianTianAiCaiPiaoIOSLJPageHandler),
    (r"/activity/go_tiantianaicaipiao_ios_wt1", channel.redirect.GoToTianTianAiCaiPiaoIOSWTZPPageHandler),
    (r"/activity/go_tiantianaicaipiao_ios_ht1", channel.redirect.GoToTianTianAiCaiPiaoIOSHuiTuiPageHandler),
    (r"/activity/go_tiantianaicaipiao_bxm1", channel.redirect.GoToTianTianAiCaiPiaoBXMPageHandler),
    (r"/activity/go_tiantianaicaipiao_ios_bxm1", channel.redirect.GoToTianTianAiCaiPiaoIOSBXMPageHandler),
    (r"/activity/go_domwatch_f1", channel.redirect.GoToDomWatchFPageHandler),
    (r"/activity/go_domwatch_m1", channel.redirect.GoToDomWatchMPageHandler),
    (r"/activity/go_lingketixudao1", channel.redirect.GoToLingKeTiXuDaoageHandler),
    (r"/activity/go_qiaohu1", channel.redirect.GoToQiaoHuPageHandler),
    (r"/activity/go_mtwm1", channel.redirect.GoToMeiTuanWaiMaiPageHandler),
    (r"/activity/go_xiangzhuanqian1", channel.redirect.GoToXiangZhuanQianPageHandler),
    (r"/activity/go_kongtiaoshan1", channel.redirect.GoToKongTiaoShanPageHandler),
    (r"/activity/go_dayangyule1", channel.redirect.GoToDaYangYuLePageHandler),
    (r"/activity/go_laobanzhang1", channel.redirect.GoToLaoBanZhangPageHandler),
    (r"/activity/go_fanliwang2", channel.redirect.GoToFanLiWang2PageHandler),
    (r"/activity/go_hnpos1", channel.redirect.GoToHeiNiuPosPageHandler),
    (r"/activity/go_tianmao1", channel.redirect.GoToTianMaoPageHandler),
    (r"/activity/go_youjie1", channel.redirect.GoToYouJiePageHandler),
    (r"/activity/go_youjie2", channel.redirect.GoToYouJie2PageHandler),
    (r"/activity/go_youjie_ht1", channel.redirect.GoToYouJieHT1PageHandler),
    (r"/activity/go_yinghuangguoji1", channel.redirect.GoToYingHuangGuoJiPageHandler),
    (r"/activity/go_qianbaojinrong1", channel.redirect.GoToQianBaoJinRongPageHandler),
    (r"/activity/go_baoxinishoubiao2", channel.redirect.GoToBaoXiNiShouBiao2PageHandler),
    (r"/activity/go_baoxinishoubiao3", channel.redirect.GoToBaoXiNiShouBiao3PageHandler),
    (r"/activity/go_baoxinishoubiao4", channel.redirect.GoToBaoXiNiShouBiao4PageHandler),
    (r"/activity/go_baoxinishoubiao_ht2", channel.redirect.GoToBaoXiNiShouBiaoHT2PageHandler),
    (r"/activity/go_baoxinishoubiao_ht3", channel.redirect.GoToBaoXiNiShouBiaoHT3PageHandler),
    (r"/activity/go_baoxinishoubiao_wowo1", channel.redirect.GoToBaoXiNiShouBiaoWoWoPageHandler),
    (r"/activity/go_baoxinishoubiao_lunbo2", channel.redirect.GoToBaoXiNiShouBiaoLunBoPageHandler),
    (r"/activity/go_yuenanshajin1", channel.redirect.GoToYueNanShaJinPageHandler),
    (r"/activity/go_dianwancheng1", channel.redirect.GoToDianWanChengPageHandler),
    (r"/activity/go_dianwancheng_h5", channel.redirect.GoToDianWanChengH5PageHandler),
    (r"/activity/go_jingpai1", channel.redirect.GoToJingPaiPageHandler),
    (r"/activity/go_naixi1", channel.redirect.GoToNaiXiPageHandler),
    (r"/activity/go_xiaobaojinrong1", channel.redirect.GoToXiaoBaoJinRongPageHandler),
    (r"/activity/go_hnbaoxini1", channel.redirect.GoToHeiNiuBaoXiNiPageHandler),
    (r"/activity/go_hnbaoxini_ht1", channel.redirect.GoToHeiNiuBaoXiNiPageHandler),
    (r"/activity/go_chaodai1", channel.redirect.GoToChaoDaiPageHandler),
    (r"/activity/go_shuisubei1", channel.redirect.GoToShuiSuBeiPageHandler),
    (r"/activity/go_hualebei1", channel.redirect.GoToHuaLeBeiPageHandler),
    (r"/activity/go_kuaishoucaipiao1", channel.redirect.GoToKuaiShouCaiPiaoPageHandler),
    (r"/activity/go_kuaishoucaipiao2", channel.redirect.GoToKuaiShouCaiPiao2PageHandler),
    (r"/activity/go_baiyingqipai1", channel.redirect.GoToBaiYingQiPaiPageHandler),
    (r"/activity/go_falaidihongjiu1", channel.redirect.GoToFaLaiDiHongJiuPageHandler),
    (r"/activity/go_kuaishan1", channel.redirect.GoToKuaiShanPageHandler),
    (r"/activity/go_tanwanqipai1", channel.redirect.GoToTanWanQiPaiPageHandler),
    (r"/activity/go_nvshenliaotian1", channel.redirect.GoToNvShenLiaoTianPageHandler),
    (r"/activity/go_niwojinrong1", channel.redirect.GoToNiWoJinRongPageHandler),
    (r"/activity/go_niwojinrong_wowo1", channel.redirect.GoToNiWoJinRongPageHandler),
    (r"/activity/go_kuaizhifu1", channel.redirect.GoToKuaiZhiFuPageHandler),
    (r"/activity/go_jianzhiying1", channel.redirect.GoToJianZhiYingPageHandler),
    (r"/activity/go_jieqiankuai1", channel.redirect.GoToJieQianKuaiPageHandler),
    (r"/activity/go_huicheliandong1", channel.redirect.GoToHuiCheLianDongPageHandler),
    (r"/activity/go_huicheliandong2", channel.redirect.GoToHuiCheLianDong2PageHandler),
    (r"/activity/go_duoxiangjinhui1", channel.redirect.GoToDuoXiangJinHuiPageHandler),
    (r"/activity/go_baolaiyule1", channel.redirect.GoToBaoLaiYuLePageHandler),
    (r"/activity/go_baolaiyule2", channel.redirect.GoToBaoLaiYuLe2PageHandler),
    (r"/activity/go_yingfuyingyu1", channel.redirect.GoToYingFuYingYuPageHandler),
    (r"/activity/go_meifuquban1", channel.redirect.GoToMeiFuQuBanPageHandler),
    (r"/activity/go_guizhoumaotai1", channel.redirect.GoToGuiZhouMaoTaiPageHandler),
    (r"/activity/go_jiehuahua1", channel.redirect.GoToJieHuaHuaPageHandler),
    (r"/activity/go_dalujietiao1", channel.redirect.GoToDaLuJieTiaoPageHandler),
    (r"/activity/go_weilan2", channel.redirect.GoToWeiLan2PageHandler),
    (r"/activity/go_niwojinrong2", channel.redirect.GoToNiWoJiRong2PageHandler),
    (r"/activity/go_zihan1", channel.redirect.GoToZiHanPageHandler),
    (r"/activity/go_jiqianjingying1", channel.redirect.GoToJiQianJingYingPageHandler),
    (r"/activity/go_haijiadianwan1", channel.redirect.GoToHaiJiaDianWanPageHandler),
    (r"/activity/go_feikejinbei1", channel.redirect.GoToFeiKeJinBeiPageHandler),
    (r"/activity/go_shanyin1", channel.redirect.GoToShanYinPageHandler),
    (r"/activity/go_yundingyule1", channel.redirect.GoToYunDingYuLePageHandler),
    (r"/activity/go_faguoXO1", channel.redirect.GoToFaGuoXOPageHandler),
    (r"/activity/go_linwang1", channel.redirect.GoToLinWangPageHandler),
    (r"/activity/go_fangnanke1", channel.redirect.GoToFangNanKePageHandler),
    (r"/activity/go_hrbfopai1", channel.redirect.GoToHaErBinPageHandler),
    (r"/activity/go_zhinengbiao1", channel.redirect.GoToZhiNengBiaoPageHandler),
    (r"/activity/go_weisikaibiao1", channel.redirect.GoToWeiSiKaiBiaoPageHandler),
    (r"/activity/go_doumengshajin1", channel.redirect.GoToDouMengShaJinPageHandler),
    (r"/activity/go_wacaixinyongka1", channel.redirect.GoToWaCaiXinYongKaPageHandler),
    (r"/activity/go_boniuyouxi1", channel.redirect.GoToBoNiuYouXiPageHandler),
    (r"/activity/go_heiniuyouqian1", channel.redirect.GoToHeiNiuYouQianPageHandler),
    (r"/activity/go_heiniuyouqian2", channel.redirect.GoToHeiNiuYouQianPageHandler),
    (r"/activity/go_heiniuyouqian3", channel.redirect.GoToHeiNiuYouQianPageHandler),
    (r"/activity/go_mianfeisongjianfei1", channel.redirect.GoToMianFeiSongJianFeiPageHandler),
    (r"/activity/go_tubatu1", channel.redirect.GoToTuBaTuPageHandler),
    (r"/activity/go_chuangyibiao1", channel.redirect.GoToChuangYiBiaoPageHandler),
    (r"/activity/go_jikaicai1", channel.redirect.GoToJiKaiCaiPageHandler),
    (r"/activity/go_dezhoupuke1", channel.redirect.GoToDeZhouPuKePageHandler),
    (r"/activity/go_zhongyicaipiao_trans1", channel.redirect.GoToZhongYiCaiPiaoPageHandler),
    (r"/activity/go_zhuoyicaipiao_trans1", channel.redirect.GoToZhuoYiCaiPiaoPageHandler),
    (r"/activity/go_shoujizhuan1", channel.redirect.GoToShouJiZhuanPageHandler),
    (r"/activity/go_cixuanfu1", channel.redirect.GoToCiXuanFuPageHandler),
    (r"/activity/go_ajiejianfei1", channel.redirect.GoToAJieJianFeiPageHandler),
    (r"/activity/go_weilan3", channel.redirect.GoToWeiLanQiPai3PageHandler),
    (r"/activity/go_daguangzongwangzhuan1", channel.redirect.GoToDaGuangZongWangZhuanPageHandler),
    (r"/activity/go_zhangshangaomen1", channel.redirect.GoToZhangShangAoMenPageHandler),
    (r"/activity/go_wangzhechuanqi1", channel.redirect.GoToWangZheChuanQiPageHandler),
    (r"/activity/go_laosibinbiao1", channel.redirect.GoToLaoSiBinBiaoPageHandler),
    (r"/activity/go_anzongwangzhuan1", channel.redirect.GoToAnZongWangZhuanPageHandler),
    (r"/activity/go_liuzongwangzhuan1", channel.redirect.GoToLiuZongWangZhuanPageHandler),
    (r"/activity/go_yanzongsongjianfei1", channel.redirect.GoToYanZongSongJianFeiPageHandler),
    (r"/activity/go_shenwangzhuan1", channel.redirect.GoToShenWangZhuanPageHandler),
    (r"/activity/go_kuaiquzhuanqian1", channel.redirect.GoToKuaiQuZhuanQianPageHandler),
    (r"/activity/go_mashangzhuanqian1", channel.redirect.GoToMaShangZhuanQianPageHandler),
    (r"/activity/go_aiqiyibaoxian1", channel.redirect.GoToAiQiYiBaoXianPageHandler),
    (r"/activity/go_jianzhizhuan1", channel.redirect.GoToJianZhiZhuanPageHandler),
    (r"/activity/go_xingyuncaipiao1", channel.redirect.GoToXingYunCaiPiaoPageHandler),
    (r"/activity/go_mamabang1", channel.redirect.GoToMaMaBangPageHandler),
    (r"/activity/go_youhaoya1", channel.redirect.GoToYouHaoYaPageHandler),
    (r"/activity/go_yunhaoqipai1", channel.redirect.GoToYunHaoQiPaiPageHandler),

    # 抽奖
    (r"/activity/get_frequency", channel.redirect.GetFrequencyHandler),
    # 大礼包
    (r"/activity/get_gift", channel.redirect.GetGiftHandler),
    # 平安车主信用卡弹窗接口
    (r"/activity/paczxyk_interface", channel.redirect.PingAnCheZhuXinYongKaInterfaceHandler),

    # 我的奖品小按钮统计
    (r"/activity/myprizes_count", channel.redirect.MyPrizesCount),
    # 没抽完的小按钮统计
    (r"/activity/prizes_count", channel.redirect.PrizesCount),


    # 蘑菇保对外链接
    (r"/activity_mgb/no_redirect1", channel.redirect.MGBNoRedirectPageHandler),
    (r"/activity_mgb/cp_redirect1", channel.redirect.MGBCaiPiaoRedirectPageHandler),
    (r"/activity_mgb/dd_redirect1", channel.redirect.MGBDiDiRedirectPageHandler),
    (r"/activity_mgb/dd_redirect_new1", channel.redirect.MGBNewDiDiRedirectPageHandler),
    (r"/activity_mgb/qgz_redirect1", channel.redirect.MGBQianGuanZiRedirectPageHandler),
    (r"/activity_mgb/mobai_redirect1", channel.redirect.MGBMoBaiRedirectPageHandler),
    (r"/activity_mgb/mtwm_redirect1", channel.redirect.MGBMeiTuanWaiMaiRedirectPageHandler),
    (r"/activity_mgb/51xyk_redirect1", channel.redirect.MGBXinYongKa51RedirectPageHandler),

    (r"/activity_mgb/trans_wangzherongyao1", channel.redirect.WangZheRongYaoTransPageHandler_MGB),
    (r"/activity_mgb/trans_quanmama1", channel.redirect.QuanMaMaTransPageHandler_MGB),
    (r"/activity_mgb/trans_dididalibao1", channel.redirect.DiDiLanJieDaLiBaoPageHandler_MGB),
    (r"/activity_mgb/trans_mtdalibao1", channel.redirect.MeiTuanDaLiBaoPageHandler_MGB),
    (r"/activity_mgb/trans_mtdalibao2", channel.redirect.MeiTuanDaLiBao2PageHandler_MGB),
    (r"/activity_mgb/trans_51xykdalibao1", channel.redirect.XinYongKa51DaLiBaoPageHandler_MGB),
    (r"/activity_mgb/trans_51xykdalibao2", channel.redirect.XinYongKa51DaLiBao2PageHandler_MGB),
    (r"/activity_mgb/trans_back_dalibao1", channel.redirect.BackDaLiBaoPageHandler_MGB),
    (r"/activity_mgb/trans_back_dalibao2", channel.redirect.BackDaLiBao2PageHandler_MGB),

    (r"/activity_mgb/tiantianaicaipiao_trans1", channel.redirect.MGBTianTianAiCaiPiaoTransPageHandler),
    (r"/activity_mgb/tiantianaicaipiao_trans2", channel.redirect.MGBTianTianAiCaiPiaoTransLJPageHandler),
    (r"/activity_mgb/tiantianaicaipiao_trans4", channel.redirect.MGBTianTianAiCaiPiaoTransHTLJPageHandler),

    (r"/activity_mgb/kuaishoucaipiao_trans1", channel.redirect.KuaiShouCaiPiaoTransPageHandler_MGB),
    (r"/activity_mgb/kuaishoucaipiao_trans2", channel.redirect.KuaiShouCaiPiaoTrans2PageHandler_MGB),

    (r"/activity_mgb/download_trans", channel.redirect.DownloadTransPageHandler_MGB),
    (r"/activity_mgb/download_trans_rrzcp", channel.redirect.RenRenZhongCaiPiaoDownloadTransPageHandler),

    (r"/activity_mgb/gojinbi4", channel.redirect.GoToJinBi4PageHandler),
    (r"/activity_mgb/godidi1", channel.redirect.GoToDiDiPageHandler),
    (r"/activity_mgb/goofo1", channel.redirect.GoToOfoPageHandler),
    (r"/activity_mgb/gojkw1", channel.redirect.GoToJieKuanWangPageHandler),
    (r"/activity_mgb/gowc1", channel.redirect.GoToWaCaiPageHandler),
    (r"/activity_mgb/gojdjk1", channel.redirect.GoToJianDanJieKuanPageHandler),
    (r"/activity_mgb/gojdjk_new1", channel.redirect.GoToJianDanJieKuanNewPageHandler),
    (r"/activity_mgb/cpdownload1", channel.redirect.MGBCaiPiaoDownloadPageHandler),
    (r"/activity_mgb/cpdownload2", channel.redirect.MGBCaiPiaoDownload2PageHandler),
    (r"/activity_mgb/cpdownloadiphone1", channel.redirect.CaiPiaoDownloadIphonePageHandler),
    (r"/activity_mgb/cpdownloadandroid1", channel.redirect.CaiPiaoDownloadAndroidPageHandler),
    (r"/activity_mgb/cpdownloadiphone2", channel.redirect.CaiPiaoDownloadIphone2PageHandler),
    (r"/activity_mgb/cpdownloadandroid2", channel.redirect.CaiPiaoDownloadAndroid2PageHandler),
    (r"/activity_mgb/gopaph1", channel.redirect.GoToPingAnPuHuiPageHandler),
    (r"/activity_mgb/gopaph2", channel.redirect.GoToPingAnPuHui2PageHandler),
    (r"/activity_mgb/goheika1", channel.redirect.GoToHeikaPageHandler),
    (r"/activity_mgb/goheika2", channel.redirect.GoToHeika2PageHandler),
    (r"/activity_mgb/goheika3", channel.redirect.GoToHeika3PageHandler),
    (r"/activity_mgb/goheika4", channel.redirect.GoToHeika4PageHandler),
    (r"/activity_mgb/goheika5", channel.redirect.GoToHeika5PageHandler),
    (r"/activity_mgb/goheika6", channel.redirect.GoToHeika6PageHandler),
    (r"/activity_mgb/goheika7", channel.redirect.GoToHeika7PageHandler),
    (r"/activity_mgb/goheika_wowo1", channel.redirect.GoToHeikaWoWoPageHandler),
    (r"/activity_mgb/goheika_51flw1", channel.redirect.GoToWoWoHeiKaPageHandler),
    (r"/activity_mgb/go_heika_CPA1", channel.redirect.GoToHeikaCPAPageHandler),
    (r"/activity_mgb/goqianguanzi1", channel.redirect.GoToQianGuanZiPageHandler),
    (r"/activity_mgb/goqianguanzi2", channel.redirect.GoToQianGuanZiPageHandler),
    (r"/activity_mgb/goqianguanzi_wowo1", channel.redirect.GoToQianGuanZiPageHandler),
    (r"/activity_mgb/goqianguanzi1_zx", channel.redirect.GoToQianGuanZiZengXianPageHandler),
    (r"/activity_mgb/gosudaizhijia1_zx", channel.redirect.GoToSuDaiZhiJiaPageHandler),
    (r"/activity_mgb/gosudaizhijia1", channel.redirect.GoToSuDaiZhiJiaPageHandler),
    (r"/activity_mgb/goxianjinka_zx", channel.redirect.GoToXianJinKaPageHandler),
    (r"/activity_mgb/goleshua1", channel.redirect.GoToLeShuaPageHandler),
    (r"/activity_mgb/goleshua_zp", channel.redirect.GoToLeShuaZhuanPanPageHandler),
    (r"/activity_mgb/go_jiaotongka1", channel.redirect.GoToJiaoTongCreditPageHandler),
    (r"/activity_mgb/go_zhongxinka1", channel.redirect.GoToZhongXinCreditPageHandler),
    (r"/activity_mgb/go_zhongxinka2", channel.redirect.GoToZhongXinCredit2PageHandler),
    (r"/activity_mgb/go_zhaoshangka1", channel.redirect.GoToZhaoShangCreditPageHandler),
    (r"/activity_mgb/go_pufaka1", channel.redirect.GoToPuFaCreditPageHandler),
    (r"/activity_mgb/go_uinpay_index1", channel.redirect.GoToEntranceCreditPageHandler),
    (r"/activity_mgb/go_mojie1", channel.redirect.GoToMoJiePageHandler),
    (r"/activity_mgb/go_caipiao_zx", channel.redirect.GoToCaiPiaoPageHandler),
    (r"/activity_mgb/go_zhaoshangka2", channel.redirect.GoToZhaoShangCredit2PageHandler),
    (r"/activity_mgb/go_minshengka1", channel.redirect.GoToMinShengCreditPageHandler),
    (r"/activity_mgb/go_minshengka2", channel.redirect.GoToMinShengCredit2PageHandler),
    (r"/activity_mgb/go_guangfaka1", channel.redirect.GoToGuangFaCreditPageHandler),
    (r"/activity_mgb/go_liminwang1", channel.redirect.GoToLiMinWangPageHandler),
    (r"/activity_mgb/go_liminwang2", channel.redirect.GoToLiMinWang2PageHandler),
    (r"/activity_mgb/go_xyqb1", channel.redirect.GoToXinYongQianBaoPageHandler),
    (r"/activity_mgb/go_xianjinka1", channel.redirect.GoToXianJinKa2PageHandler),
    (r"/activity_mgb/go_wolaidai1", channel.redirect.GoToWoLaiDaiPageHandler),
    (r"/activity_mgb/go_yiyuanduobao_ios1", channel.redirect.GoToYiYuanDuoBaoIosPageHandler),
    (r"/activity_mgb/go_yiyuanduobao_android1", channel.redirect.GoToYiYuanDuoBaoAndroidPageHandler),
    (r"/activity_mgb/go_jiedianqian1", channel.redirect.GoToJieDianQianPageHandler),
    (r"/activity_mgb/go_jiedianqian2", channel.redirect.GoToJieDianQian2PageHandler),
    (r"/activity_mgb/go_jiedianqian3", channel.redirect.GoToJieDianQian3PageHandler),
    (r"/activity_mgb/go_jiedianqian_ht2", channel.redirect.GoToJieDianQianHT2PageHandler),
    (r"/activity_mgb/go_xingxingqiandai1", channel.redirect.GoToXingXingQianDaiPageHandler),
    (r"/activity_mgb/go_vipkid1", channel.redirect.GoToVipKidPageHandler),
    (r"/activity_mgb/go_vipkid1_1", channel.redirect.GoToVipKid1_1PageHandler),
    (r"/activity_mgb/go_vipkid1_2", channel.redirect.GoToVipKid1_2PageHandler),
    (r"/activity_mgb/go_vipkid1_3", channel.redirect.GoToVipKid1_3PageHandler),
    (r"/activity_mgb/go_huanleduobao_android1", channel.redirect.GoToHuanLeDuoBaoAndroidPageHandler),
    (r"/activity_mgb/go_huanleduobao_ios1", channel.redirect.GoToHuanLeDuoBaoIOSPageHandler),
    (r"/activity_mgb/go_mobai1", channel.redirect.GoToMoBaiPageHandler),
    (r"/activity_mgb/go_guangdaka1", channel.redirect.GoToGuangDaKaPageHandler),
    (r"/activity_mgb/go_luolizhajinhua1", channel.redirect.GoToLuoLiZhaJinHuaPageHandler),
    (r"/activity_mgb/go_quanmama1", channel.redirect.GoToQuanMaMaPageHandler),
    (r"/activity_mgb/go_quanmama2", channel.redirect.GoToQuanMaMa2PageHandler),
    (r"/activity_mgb/go_yirendai1", channel.redirect.GoToYiRenDaiPageHandler),
    (r"/activity_mgb/go_dazhongdianping1", channel.redirect.GoToDaZhongDianPingPageHandler),
    (r"/activity_mgb/go_laicaicaipiao1", channel.redirect.GoToLaiCaiCaiPiaoPageHandler),
    (r"/activity_mgb/go_xianjinxia1", channel.redirect.GoToXianJinXiaPageHandler),
    (r"/activity_mgb/go_jinbeiqipai_android1", channel.redirect.GoToJinBeiQiPaiAndroidPageHandler),
    (r"/activity_mgb/go_jinbeiqipai_ios1", channel.redirect.GoToJinBeiQiPaiIOSPageHandler),
    (r"/activity_mgb/go_wanhaocaipiao1", channel.redirect.GoToWanHaoCaiPiaoPageHandler),
    (r"/activity_mgb/go_wanhaocaipiao2", channel.redirect.GoToWanHaoCaiPiao2PageHandler),
    (r"/activity_mgb/go_baoxinishoubiao1", channel.redirect.GoToBaoXiNiShouBiaoPageHandler),
    (r"/activity_mgb/go_yinhezhixing1", channel.redirect.GoToYinHeZhiXingPageHandler),
    (r"/activity_mgb/go_fopaiheiyaoshi1", channel.redirect.GoToFoPaiHeiYaoShiPageHandler),
    (r"/activity_mgb/go_pixiu1", channel.redirect.GoToPiXiuPageHandler),
    (r"/activity_mgb/go_yicaidao1", channel.redirect.GoToYiCaiDaoPageHandler),
    (r"/activity_mgb/go_yicaidao_gxcdb1", channel.redirect.GoToGongXiangChongDianBaoYiCaiDaoPageHandler),
    (r"/activity_mgb/go_paczxyk1", channel.redirect.GoToPingAnXinYongKaYDPageHandler),
    (r"/activity_mgb/go_buyudashi1", channel.redirect.GoToBuYuDaShiPageHandler),
    (r"/activity_mgb/go_koudaiauction_ios1", channel.redirect.GoToKouDaiAuctionIOSPageHandler),
    (r"/activity_mgb/go_koudaiauction_android1", channel.redirect.GoToKouDaiAuctionAndroidPageHandler),
    (r"/activity_mgb/go_huaerjie1", channel.redirect.GoToHuaErJiePageHandler),
    (r"/activity_mgb/go_jinronghui1", channel.redirect.GoToJinRongHuiPageHandler),
    (r"/activity_mgb/go_heiniudaikuan1", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity_mgb/go_heiniudaikuan2", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity_mgb/go_heiniudaikuan3", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity_mgb/go_heiniudaikuan4", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity_mgb/go_heiniudaikuan_lunbo", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity_mgb/go_heiniudaikuan_wowo", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity_mgb/go_jinshancaipiao1", channel.redirect.GoToJinShanCaiPiaoPageHandler),
    (r"/activity_mgb/go_kuaiyihua1", channel.redirect.GoToKuaiYiHuaPageHandler),
    (r"/activity_mgb/go_taoxinwen1", channel.redirect.GoToTaoXinWenPageHandler),
    (r"/activity_mgb/go_quanminduobao_ios1", channel.redirect.GoToQuanMingDuoBaoIOSPageHandler),
    (r"/activity_mgb/go_quanminduobao_android1", channel.redirect.GoToQuanMingDuoBaoAndroidPageHandler),
    (r"/activity_mgb/go_qiuqiudoudizhu1", channel.redirect.GoToQiuQiuDouDiZhuPageHandler),
    (r"/activity_mgb/go_kuhuasuoping1", channel.redirect.GoToKuHuaSuoPingPageHandler),
    (r"/activity_mgb/go_shanghaiyhxyk1", channel.redirect.GoToShangHaiYinHangXinYongKaPageHandler),
    (r"/activity_mgb/go_leshua2", channel.redirect.GoToLeShua2PageHandler),
    (r"/activity_mgb/go_leshua_out", channel.redirect.GoToLeShuaOutPageHandler),
    (r"/activity_mgb/go_qianyoulu1", channel.redirect.GoToQianYouLuPageHandler),
    (r"/activity_mgb/go_hulishajin1", channel.redirect.GoToHuLiShaJinPageHandler),
    (r"/activity_mgb/go_heiyaoshi_pixiu1", channel.redirect.GoToHeiYaoShiPiXiuPageHandler),
    (r"/activity_mgb/go_wonenglicai1", channel.redirect.GoToWoNengLiCaiPageHandler),
    (r"/activity_mgb/go_heiniubaoxian1", channel.redirect.GoToHeiNiuBaoXianPageHandler),
    (r"/activity_mgb/go_shandai1", channel.redirect.GoToShanDaiPageHandler),
    (r"/activity_mgb/go_bingsineiku1", channel.redirect.GoToBingSiNeiKuPageHandler),
    (r"/activity_mgb/go_T_shirtman1", channel.redirect.GoToTShirtManPageHandler),
    (r"/activity_mgb/go_hengxinmetal1", channel.redirect.GoToHengXinMetalPageHandler),
    (r"/activity_mgb/go_quanminauction_ios1", channel.redirect.GoToQuanMinAuctionPageHandler),
    (r"/activity_mgb/go_quanminauction_android1", channel.redirect.GoToQuanMinAuctionPageHandler),
    (r"/activity_mgb/go_koudaijc_ios1", channel.redirect.GoToKouDaiJingCaiIOSPageHandler),
    (r"/activity_mgb/go_koudaijc_android1", channel.redirect.GoToKouDaiJingCaiAndroidPageHandler),
    (r"/activity_mgb/go_wanrendoudizhu1", channel.redirect.GoToWanRenDouDiZhuPageHandler),
    (r"/activity_mgb/go_wanrendoudizhu2", channel.redirect.GoToWanRenDouDiZhu2PageHandler),
    (r"/activity_mgb/go_wanrendoudizhu_zp", channel.redirect.GoToWanRenDouDiZhuZPPageHandler),
    (r"/activity_mgb/go_daishangqian1", channel.redirect.GoToDaiShangQianPageHandler),
    (r"/activity_mgb/go_yiyuanduobao2_android", channel.redirect.GoToXYDuoBao2AndroidPageHandler),
    (r"/activity_mgb/go_hengxinmetal1_zp", channel.redirect.GoToHengXingMetalZP1PageHandler),
    (r"/activity_mgb/go_wangzherongyao1", channel.redirect.GoToWangZheRongYaoKaPageHandler),
    (r"/activity_mgb/go_baoxiniqinglvbiao1", channel.redirect.GoToBaoXiNiQingLvBiaoPageHandler),
    (r"/activity_mgb/go_tiantianzhajinhua1", channel.redirect.GoToTianTianZhaJinHuaPageHandler),
    (r"/activity_mgb/go_tengxunlicaitong1", channel.redirect.GoToTengXunLiCaiTongPageHandler),
    (r"/activity_mgb/go_xiangqiandai1", channel.redirect.GoToXiangQianDaiPageHandler),
    (r"/activity_mgb/go_baidujinrong1", channel.redirect.GoToBaiDuJinRongPageHandler),
    (r"/activity_mgb/go_360jietiao1", channel.redirect.GoTo360JieTiaoPageHandler),
    (r"/activity_mgb/go_360jietiao_gxcdb1", channel.redirect.GoToGongXiangChongDianBao360JieTiaoPageHandler),
    (r"/activity_mgb/go_yongqianbao1", channel.redirect.GoToYongQianBaoPageHandler),
    (r"/activity_mgb/go_lvshoujianfei1", channel.redirect.GoToLvShouJianFeiPageHandler),
    (r"/activity_mgb/go_binzhiheika1", channel.redirect.GoToBinZhiHeiKaPageHandler),
    (r"/activity_mgb/go_dianwanchengzhajinhua1", channel.redirect.GoToDianWanChengZhaJinHuaPageHandler),
    (r"/activity_mgb/go_songjiangdai1", channel.redirect.GoToSongJiangDaiPageHandler),
    (r"/activity_mgb/go_kaixinqianbao1", channel.redirect.GoToKaiXinQianBaoPageHandler),
    (r"/activity_mgb/go_kaniu1", channel.redirect.GoToKaNiuPageHandler),
    (r"/activity_mgb/go_jiekuanzhuanjia1", channel.redirect.GoToJieKuanZhuanJiaPageHandler),
    (r"/activity_mgb/go_yinghuangyule1", channel.redirect.GoToYingHuangYuLePageHandler),
    (r"/activity_mgb/go_360daikuan1", channel.redirect.GoTo360DaiKuanPageHandler),
    (r"/activity_mgb/go_51xinyongkaguanjia1", channel.redirect.GoTo51XinYongKaGuanJiaPageHandler),
    (r"/activity_mgb/go_51xinyongkaguanjia2", channel.redirect.GoTo51XinYongKaGuanJia2PageHandler),
    (r"/activity_mgb/go_51xinyongkaguanjia3", channel.redirect.GoTo51XinYongKaGuanJia3PageHandler),
    (r"/activity_mgb/go_51xinyongkaguanjia_wowo1", channel.redirect.GoTo51XinYongKaGuanJiaWoWoPageHandler),
    (r"/activity_mgb/go_niwodai1", channel.redirect.GoToNiWoDaiPageHandler),
    (r"/activity_mgb/go_xianjindai1", channel.redirect.GoToXianJinDaiPageHandler),
    (r"/activity_mgb/go_rong360_1", channel.redirect.GoToRong360PageHandler),
    (r"/activity_mgb/go_rong360_zp", channel.redirect.GoToRong360ZPPageHandler),
    (r"/activity_mgb/go_rong360_lunbo", channel.redirect.GoToRong360LunBoPageHandler),
    (r"/activity_mgb/go_leshua3", channel.redirect.GoToLeShua3PageHandler),
    (r"/activity_mgb/go_leshua_zp3", channel.redirect.GoToLeShuaZP3PageHandler),
    (r"/activity_mgb/go_leshua_xq_zp3", channel.redirect.GoToLeShuaXiangQianZP3PageHandler),
    (r"/activity_mgb/go_leshua_zp", channel.redirect.GoToLeShuaZPPageHandler),
    (r"/activity_mgb/go_leshua_ht4", channel.redirect.GoToLeShuaHT4PageHandler),
    (r"/activity_mgb/go_shandianpaimai1", channel.redirect.GoToShanDianPaiMaiPageHandler),
    (r"/activity_mgb/go_wangyiguijinshu1", channel.redirect.GoToWangYiGuiJinShuPageHandler),
    (r"/activity_mgb/go_mojie2", channel.redirect.GoToMoJie2PageHandler),
    (r"/activity_mgb/go_xinerfu1", channel.redirect.GoToXinErFuPageHandler),
    (r"/activity_mgb/go_tongchengyeyou1", channel.redirect.GoToTongChengYeYouPageHandler),
    (r"/activity_mgb/go_360daikuan2", channel.redirect.GoTo360DaiKuan2PageHandler),
    (r"/activity_mgb/go_fanliwang1", channel.redirect.GoToFanLiWangPageHandler),
    (r"/activity_mgb/go_lanyueqipai1", channel.redirect.GoToLanYueQiPaiPageHandler),
    (r"/activity_mgb/go_weijiaoyi1", channel.redirect.GoToWeiJiaoYiPageHandler),
    (r"/activity_mgb/go_hnfopai1", channel.redirect.GoToHeiNiuFoPaiPageHandler),
    (r"/activity_mgb/go_hnfopai2", channel.redirect.GoToHeiNiuFoPai2PageHandler),
    (r"/activity_mgb/go_dingdangkuaiyao1", channel.redirect.GoToDingDangKuaiYaoPageHandler),
    (r"/activity_mgb/go_shandianjiangjia1", channel.redirect.GoToShanDianJiangJiaPageHandler),
    (r"/activity_mgb/go_boluodai1", channel.redirect.GoToJuJiuPeiPageHandler),
    (r"/activity_mgb/go_zhuanqian1", channel.redirect.GoToZhuanQianPageHandler),
    (r"/activity_mgb/go_daiba1", channel.redirect.GoToDaiBaPageHandler),
    (r"/activity_mgb/go_daiba_ht1", channel.redirect.GoToDaiBaHT1PageHandler),
    (r"/activity_mgb/go_dingguagua1", channel.redirect.GoToDingGuaGuaPageHandler),
    (r"/activity_mgb/go_tuhaodayingjia1", channel.redirect.GoToTuHaoDaYingJiaPageHandler),
    (r"/activity_mgb/go_xianjinjiekuan1", channel.redirect.GoToXianJinJieKuanPageHandler),
    (r"/activity_mgb/go_pengboyule1", channel.redirect.GoToPengBoYuLePageHandler),
    (r"/activity_mgb/go_zhaoshangka3", channel.redirect.GoToZhaoShangCredit3PageHandler),
    (r"/activity_mgb/go_tiantianaicaipiao1", channel.redirect.GoToTianTianAiCaiPiaoPageHandler),
    (r"/activity_mgb/go_tiantianaicaipiao_lj1", channel.redirect.GoToTianTianAiCaiPiaoLJPageHandler),
    (r"/activity_mgb/go_tiantianaicaipiao_wt1", channel.redirect.GoToTianTianAiCaiPiaoWTZPPageHandler),
    (r"/activity_mgb/go_tiantianaicaipiao_ht1", channel.redirect.GoToTianTianAiCaiPiaoHuiTuiPageHandler),
    (r"/activity_mgb/go_tiantianaicaipiao_ios1", channel.redirect.GoToTianTianAiCaiPiaoIOSPageHandler),
    (r"/activity_mgb/go_tiantianaicaipiao_ios_lj1", channel.redirect.GoToTianTianAiCaiPiaoIOSLJPageHandler),
    (r"/activity_mgb/go_tiantianaicaipiao_ios_wt1", channel.redirect.GoToTianTianAiCaiPiaoIOSWTZPPageHandler),
    (r"/activity_mgb/go_tiantianaicaipiao_ios_ht1", channel.redirect.GoToTianTianAiCaiPiaoIOSHuiTuiPageHandler),
    (r"/activity_mgb/go_domwatch_f1", channel.redirect.GoToDomWatchFPageHandler),
    (r"/activity_mgb/go_domwatch_m1", channel.redirect.GoToDomWatchMPageHandler),
    (r"/activity_mgb/go_lingketixudao1", channel.redirect.GoToLingKeTiXuDaoageHandler),
    (r"/activity_mgb/go_qiaohu1", channel.redirect.GoToQiaoHuPageHandler),
    (r"/activity_mgb/go_mtwm1", channel.redirect.GoToMeiTuanWaiMaiPageHandler),
    (r"/activity_mgb/go_xiangzhuanqian1", channel.redirect.GoToXiangZhuanQianPageHandler),
    (r"/activity_mgb/go_kongtiaoshan1", channel.redirect.GoToKongTiaoShanPageHandler),
    (r"/activity_mgb/go_dayangyule1", channel.redirect.GoToDaYangYuLePageHandler),
    (r"/activity_mgb/go_laobanzhang1", channel.redirect.GoToLaoBanZhangPageHandler),
    (r"/activity_mgb/go_fanliwang2", channel.redirect.GoToFanLiWang2PageHandler),
    (r"/activity_mgb/go_hnpos1", channel.redirect.GoToHeiNiuPosPageHandler),
    (r"/activity_mgb/go_tianmao1", channel.redirect.GoToTianMaoPageHandler),
    (r"/activity_mgb/go_youjie1", channel.redirect.GoToYouJiePageHandler),
    (r"/activity_mgb/go_youjie2", channel.redirect.GoToYouJie2PageHandler),
    (r"/activity_mgb/go_youjie_ht1", channel.redirect.GoToYouJieHT1PageHandler),
    (r"/activity_mgb/go_yinghuangguoji1", channel.redirect.GoToYingHuangGuoJiPageHandler),
    (r"/activity_mgb/go_qianbaojinrong1", channel.redirect.GoToQianBaoJinRongPageHandler),
    (r"/activity_mgb/go_baoxinishoubiao2", channel.redirect.GoToBaoXiNiShouBiao2PageHandler),
    (r"/activity_mgb/go_baoxinishoubiao3", channel.redirect.GoToBaoXiNiShouBiao3PageHandler),
    (r"/activity_mgb/go_baoxinishoubiao4", channel.redirect.GoToBaoXiNiShouBiao4PageHandler),
    (r"/activity_mgb/go_baoxinishoubiao_ht2", channel.redirect.GoToBaoXiNiShouBiaoHT2PageHandler),
    (r"/activity_mgb/go_baoxinishoubiao_ht3", channel.redirect.GoToBaoXiNiShouBiaoHT3PageHandler),
    (r"/activity_mgb/go_baoxinishoubiao_wowo1", channel.redirect.GoToBaoXiNiShouBiaoWoWoPageHandler),
    (r"/activity_mgb/go_baoxinishoubiao_lunbo2", channel.redirect.GoToBaoXiNiShouBiaoLunBoPageHandler),
    (r"/activity_mgb/go_yuenanshajin1", channel.redirect.GoToYueNanShaJinPageHandler),
    (r"/activity_mgb/go_dianwancheng1", channel.redirect.GoToDianWanChengPageHandler),
    (r"/activity_mgb/go_dianwancheng_h5", channel.redirect.GoToDianWanChengH5PageHandler),
    (r"/activity_mgb/go_jingpai1", channel.redirect.GoToJingPaiPageHandler),
    (r"/activity_mgb/go_naixi1", channel.redirect.GoToNaiXiPageHandler),
    (r"/activity_mgb/go_xiaobaojinrong1", channel.redirect.GoToXiaoBaoJinRongPageHandler),
    (r"/activity_mgb/go_hnbaoxini1", channel.redirect.GoToHeiNiuBaoXiNiPageHandler),
    (r"/activity_mgb/go_hnbaoxini_ht1", channel.redirect.GoToHeiNiuBaoXiNiPageHandler),
    (r"/activity_mgb/go_chaodai1", channel.redirect.GoToChaoDaiPageHandler),
    (r"/activity_mgb/go_shuisubei1", channel.redirect.GoToShuiSuBeiPageHandler),
    (r"/activity_mgb/go_hualebei1", channel.redirect.GoToHuaLeBeiPageHandler),
    (r"/activity_mgb/go_kuaishoucaipiao1", channel.redirect.GoToKuaiShouCaiPiaoPageHandler),
    (r"/activity_mgb/go_kuaishoucaipiao2", channel.redirect.GoToKuaiShouCaiPiao2PageHandler),
    (r"/activity_mgb/go_baiyingqipai1", channel.redirect.GoToBaiYingQiPaiPageHandler),
    (r"/activity_mgb/go_falaidihongjiu1", channel.redirect.GoToFaLaiDiHongJiuPageHandler),
    (r"/activity_mgb/go_kuaishan1", channel.redirect.GoToKuaiShanPageHandler),
    (r"/activity_mgb/go_tanwanqipai1", channel.redirect.GoToTanWanQiPaiPageHandler),
    (r"/activity_mgb/go_nvshenliaotian1", channel.redirect.GoToNvShenLiaoTianPageHandler),
    (r"/activity_mgb/go_niwojinrong1", channel.redirect.GoToNiWoJinRongPageHandler),
    (r"/activity_mgb/go_niwojinrong_wowo1", channel.redirect.GoToNiWoJinRongPageHandler),
    (r"/activity_mgb/go_kuaizhifu1", channel.redirect.GoToKuaiZhiFuPageHandler),
    (r"/activity_mgb/go_jianzhiying1", channel.redirect.GoToJianZhiYingPageHandler),
    (r"/activity_mgb/go_jieqiankuai1", channel.redirect.GoToJieQianKuaiPageHandler),
    (r"/activity_mgb/go_huicheliandong1", channel.redirect.GoToHuiCheLianDongPageHandler),
    (r"/activity_mgb/go_huicheliandong2", channel.redirect.GoToHuiCheLianDong2PageHandler),
    (r"/activity_mgb/go_duoxiangjinhui1", channel.redirect.GoToDuoXiangJinHuiPageHandler),
    (r"/activity_mgb/go_baolaiyule1", channel.redirect.GoToBaoLaiYuLePageHandler),
    (r"/activity_mgb/go_baolaiyule2", channel.redirect.GoToBaoLaiYuLe2PageHandler),
    (r"/activity_mgb/go_yingfuyingyu1", channel.redirect.GoToYingFuYingYuPageHandler),
    (r"/activity_mgb/go_meifuquban1", channel.redirect.GoToMeiFuQuBanPageHandler),
    (r"/activity_mgb/go_guizhoumaotai1", channel.redirect.GoToGuiZhouMaoTaiPageHandler),
    (r"/activity_mgb/go_jiehuahua1", channel.redirect.GoToJieHuaHuaPageHandler),
    (r"/activity_mgb/go_dalujietiao1", channel.redirect.GoToDaLuJieTiaoPageHandler),
    (r"/activity_mgb/go_weilan2", channel.redirect.GoToWeiLan2PageHandler),
    (r"/activity_mgb/go_niwojinrong2", channel.redirect.GoToNiWoJiRong2PageHandler),
    (r"/activity_mgb/go_zihan1", channel.redirect.GoToZiHanPageHandler),
    (r"/activity_mgb/go_jiqianjingying1", channel.redirect.GoToJiQianJingYingPageHandler),
    (r"/activity_mgb/go_haijiadianwan1", channel.redirect.GoToHaiJiaDianWanPageHandler),
    (r"/activity_mgb/go_feikejinbei1", channel.redirect.GoToFeiKeJinBeiPageHandler),
    (r"/activity_mgb/go_shanyin1", channel.redirect.GoToShanYinPageHandler),
    (r"/activity_mgb/go_yundingyule1", channel.redirect.GoToYunDingYuLePageHandler),
    (r"/activity_mgb/go_faguoXO1", channel.redirect.GoToFaGuoXOPageHandler),
    (r"/activity_mgb/go_linwang1", channel.redirect.GoToLinWangPageHandler),
    (r"/activity_mgb/go_fangnanke1", channel.redirect.GoToFangNanKePageHandler),
    (r"/activity_mgb/go_hrbfopai1", channel.redirect.GoToHaErBinPageHandler),
    (r"/activity_mgb/go_zhinengbiao1", channel.redirect.GoToZhiNengBiaoPageHandler),
    (r"/activity_mgb/go_weisikaibiao1", channel.redirect.GoToWeiSiKaiBiaoPageHandler),
    (r"/activity_mgb/go_doumengshajin1", channel.redirect.GoToDouMengShaJinPageHandler),
    (r"/activity_mgb/go_wacaixinyongka1", channel.redirect.GoToWaCaiXinYongKaPageHandler),
    (r"/activity_mgb/go_boniuyouxi1", channel.redirect.GoToBoNiuYouXiPageHandler),
    (r"/activity_mgb/go_heiniuyouqian1", channel.redirect.GoToHeiNiuYouQianPageHandler),
    (r"/activity_mgb/go_heiniuyouqian2", channel.redirect.GoToHeiNiuYouQianPageHandler),
    (r"/activity_mgb/go_heiniuyouqian3", channel.redirect.GoToHeiNiuYouQianPageHandler),
    (r"/activity_mgb/go_mianfeisongjianfei1", channel.redirect.GoToMianFeiSongJianFeiPageHandler),
    (r"/activity_mgb/go_tubatu1", channel.redirect.GoToTuBaTuPageHandler),
    (r"/activity_mgb/go_chuangyibiao1", channel.redirect.GoToChuangYiBiaoPageHandler),
    (r"/activity_mgb/go_jikaicai1", channel.redirect.GoToJiKaiCaiPageHandler),
    (r"/activity_mgb/go_dezhoupuke1", channel.redirect.GoToDeZhouPuKePageHandler),
    (r"/activity_mgb/go_zhongyicaipiao_trans1", channel.redirect.GoToZhongYiCaiPiaoPageHandler),
    (r"/activity_mgb/go_zhuoyicaipiao_trans1", channel.redirect.GoToZhuoYiCaiPiaoPageHandler),
    (r"/activity_mgb/go_shoujizhuan1", channel.redirect.GoToShouJiZhuanPageHandler),
    (r"/activity_mgb/go_cixuanfu1", channel.redirect.GoToCiXuanFuPageHandler),
    (r"/activity_mgb/go_ajiejianfei1", channel.redirect.GoToAJieJianFeiPageHandler),
    (r"/activity_mgb/go_weilan3", channel.redirect.GoToWeiLanQiPai3PageHandler),
    (r"/activity_mgb/go_daguangzongwangzhuan1", channel.redirect.GoToDaGuangZongWangZhuanPageHandler),
    (r"/activity_mgb/go_zhangshangaomen1", channel.redirect.GoToZhangShangAoMenPageHandler),
    (r"/activity_mgb/go_wangzhechuanqi1", channel.redirect.GoToWangZheChuanQiPageHandler),
    (r"/activity_mgb/go_laosibinbiao1", channel.redirect.GoToLaoSiBinBiaoPageHandler),
    (r"/activity_mgb/go_anzongwangzhuan1", channel.redirect.GoToAnZongWangZhuanPageHandler),
    (r"/activity_mgb/go_liuzongwangzhuan1", channel.redirect.GoToLiuZongWangZhuanPageHandler),
    (r"/activity_mgb/go_yanzongsongjianfei1", channel.redirect.GoToYanZongSongJianFeiPageHandler),
    (r"/activity_mgb/go_shenwangzhuan1", channel.redirect.GoToShenWangZhuanPageHandler),
    (r"/activity_mgb/go_kuaiquzhuanqian1", channel.redirect.GoToKuaiQuZhuanQianPageHandler),
    (r"/activity_mgb/go_mashangzhuanqian1", channel.redirect.GoToMaShangZhuanQianPageHandler),
    (r"/activity_mgb/go_aiqiyibaoxian1", channel.redirect.GoToAiQiYiBaoXianPageHandler),
    (r"/activity_mgb/go_jianzhizhuan1", channel.redirect.GoToJianZhiZhuanPageHandler),
    (r"/activity_mgb/go_xingyuncaipiao1", channel.redirect.GoToXingYunCaiPiaoPageHandler),
    (r"/activity_mgb/go_mamabang1", channel.redirect.GoToMaMaBangPageHandler),
    (r"/activity_mgb/go_youhaoya1", channel.redirect.GoToYouHaoYaPageHandler),
    (r"/activity_mgb/go_yunhaoqipai1", channel.redirect.GoToYunHaoQiPaiPageHandler),

    # 蘑菇保抽奖
    (r"/activity_mgb/get_frequency", channel.redirect.GetFrequencyHandler),

    # 推广抽奖
    (r"/activity/prize_redirect1", channel.redirect.PrizePageHandler),
    # 推广广告位
    (r"/activity/prize_fls_redirect1", channel.redirect.PrizeFuLiShePageHandler),
    (r"/activity/prize_interface1", channel.redirect.PrizeInterfaceHandler),
    (r"/activity/my_prizes_interface1", channel.redirect.MyPrizesInterfaceHandler),

    (r"/activity/prize_trans_wangzherongyao1", channel.redirect.PrizeWangZheRongYaoTransPageHandler),
    (r"/activity/prize_trans_quanmama1", channel.redirect.PrizeQuanMaMaTransPageHandler),

    (r"/activity/prize_tiantianaicaipiao_trans3", channel.redirect.TianTianAiCaiPiaoTransWTPageHandler),

    (r"/activity/prize_kuaishoucaipiao_trans1", channel.redirect.KuaiShouCaiPiaoTransPageHandler_WT),

    (r"/activity/prize_download_trans", channel.redirect.PrizeDownloadTransPageHandler),
    (r"/activity/prize_download_trans_rrzcp", channel.redirect.RenRenZhongCaiPiaoDownloadTransPageHandler),

    # (r"/activity/prize_gojinbi4", channel.redirect.GoToJinBi4PageHandler),
    (r"/activity/prize_godidi1", channel.redirect.GoToDiDiPageHandler),
    (r"/activity/prize_goofo1", channel.redirect.GoToOfoPageHandler),
    (r"/activity/prize_gojkw1", channel.redirect.GoToJieKuanWangPageHandler),
    (r"/activity/prize_gowc1", channel.redirect.GoToWaCaiPageHandler),
    (r"/activity/prize_gojdjk1", channel.redirect.GoToJianDanJieKuanPageHandler),
    (r"/activity/prize_gojdjk_new1", channel.redirect.GoToJianDanJieKuanNewPageHandler),
    (r"/activity/prize_cpdownload1", channel.redirect.PrizeCaiPiaoDownloadPageHandler),
    # (r"/activity/prize_cpdownload2", channel.redirect.CaiPiaoDownload2PageHandler),
    # (r"/activity/prize_cpdownload3", channel.redirect.CaiPiaoDownload3PageHandler),
    (r"/activity/prize_cpdownloadiphone1", channel.redirect.CaiPiaoDownloadIphonePageHandler),
    (r"/activity/prize_cpdownloadandroid1", channel.redirect.CaiPiaoDownloadAndroidPageHandler),
    # (r"/activity/prize_cpdownloadiphone2", channel.redirect.CaiPiaoDownloadIphone2PageHandler),
    # (r"/activity/prize_cpdownloadandroid2", channel.redirect.CaiPiaoDownloadAndroid2PageHandler),
    # (r"/activity/prize_cpdownloadiphone3", channel.redirect.CaiPiaoDownloadIphone3PageHandler),
    # (r"/activity/prize_cpdownloadandroid3", channel.redirect.CaiPiaoDownloadAndroid3PageHandler),
    (r"/activity/prize_gopaph1", channel.redirect.GoToPingAnPuHuiPageHandler),
    (r"/activity/prize_gopaph2", channel.redirect.GoToPingAnPuHui2PageHandler),
    (r"/activity/prize_goheika1", channel.redirect.GoToHeikaPageHandler),
    (r"/activity/prize_goheika2", channel.redirect.GoToHeika2PageHandler),
    (r"/activity/prize_goheika3", channel.redirect.GoToHeika3PageHandler),
    (r"/activity/prize_goheika4", channel.redirect.GoToHeika4PageHandler),
    (r"/activity/prize_goheika5", channel.redirect.GoToHeika5PageHandler),
    (r"/activity/prize_goheika6", channel.redirect.GoToHeika6PageHandler),
    (r"/activity/prize_goheika7", channel.redirect.GoToHeika7PageHandler),
    (r"/activity/prize_goheika_wowo1", channel.redirect.GoToHeikaWoWoPageHandler),
    (r"/activity/prize_goheika_51flw1", channel.redirect.GoToWoWoHeiKaPageHandler),
    (r"/activity/prize_go_heika_CPA1", channel.redirect.GoToHeikaCPAPageHandler),
    (r"/activity/prize_gosudaizhijia1", channel.redirect.GoToSuDaiZhiJiaPageHandler),
    (r"/activity/prize_goqianguanzi1", channel.redirect.GoToQianGuanZiPageHandler),
    (r"/activity/prize_goqianguanzi2", channel.redirect.GoToQianGuanZiPageHandler),
    (r"/activity/prize_goqianguanzi_wowo1", channel.redirect.GoToQianGuanZiPageHandler),
    # (r"/activity/prize_goqianguanzi1_zx", channel.redirect.GoToQianGuanZiZengXianPageHandler),
    # (r"/activity/prize_gosudaizhijia1_zx", channel.redirect.GoToSuDaiZhiJiaPageHandler),
    # (r"/activity/prize_gopinganwacai1_zx", channel.redirect.GoToPingAnWaCaiPageHandler),
    # (r"/activity/prize_gopinganpuhui1_zx", channel.redirect.GoToPAPuHuiDaiKuanWangPageHandler),
    # (r"/activity/prize_gojiekuanzhuangjia1_zx", channel.redirect.GoToJieKuanZhuangJiaPageHandler),
    # (r"/activity/prize_go2345daikuanwang1_zx", channel.redirect.GoTo2345DaiKuanWangPageHandler),
    # (r"/activity/prize_goxianjinka_zx", channel.redirect.GoToXianJinKaPageHandler),
    (r"/activity/prize_goleshua1", channel.redirect.GoToLeShuaPageHandler),
    (r"/activity/prize_goleshua_zp", channel.redirect.GoToLeShuaZhuanPanPageHandler),
    (r"/activity/prize_go_jiaotongka1", channel.redirect.GoToJiaoTongCreditPageHandler),
    (r"/activity/prize_go_zhongxinka1", channel.redirect.GoToZhongXinCreditPageHandler),
    (r"/activity/prize_go_zhongxinka2", channel.redirect.GoToZhongXinCredit2PageHandler),
    (r"/activity/prize_go_zhaoshangka1", channel.redirect.GoToZhaoShangCreditPageHandler),
    (r"/activity/prize_go_pufaka1", channel.redirect.GoToPuFaCreditPageHandler),
    (r"/activity/prize_go_uinpay_index1", channel.redirect.GoToEntranceCreditPageHandler),
    (r"/activity/prize_go_mojie1", channel.redirect.GoToMoJiePageHandler),
    # (r"/activity/prize_go_caipiao_zx", channel.redirect.GoToCaiPiaoPageHandler),
    # (r"/activity/prize_go_paxyk_yd", channel.redirect.GoToPingAnXinYongKaYDPageHandler),
    # (r"/activity/prize_go_paxyk_pc", channel.redirect.GoToPingAnXinYongKaPCPageHandler),
    (r"/activity/prize_go_zhaoshangka2", channel.redirect.GoToZhaoShangCredit2PageHandler),
    (r"/activity/prize_go_minshengka1", channel.redirect.GoToMinShengCreditPageHandler),
    (r"/activity/prize_go_minshengka2", channel.redirect.GoToMinShengCredit2PageHandler),
    (r"/activity/prize_go_guangfaka1", channel.redirect.GoToGuangFaCreditPageHandler),
    (r"/activity/prize_go_liminwang1", channel.redirect.GoToLiMinWangPageHandler),
    (r"/activity/prize_go_liminwang2", channel.redirect.GoToLiMinWang2PageHandler),
    (r"/activity/prize_go_xyqb1", channel.redirect.GoToXinYongQianBaoPageHandler),
    (r"/activity/prize_go_xianjinka1", channel.redirect.GoToXianJinKa2PageHandler),
    (r"/activity/prize_go_wolaidai1", channel.redirect.GoToWoLaiDaiPageHandler),
    (r"/activity/prize_go_yiyuanduobao_ios1", channel.redirect.GoToYiYuanDuoBaoIosPageHandler),
    (r"/activity/prize_go_yiyuanduobao_android1", channel.redirect.GoToYiYuanDuoBaoAndroidPageHandler),
    (r"/activity/prize_go_jiedianqian1", channel.redirect.GoToJieDianQianPageHandler),
    (r"/activity/prize_go_jiedianqian2", channel.redirect.GoToJieDianQian2PageHandler),
    (r"/activity/prize_go_jiedianqian3", channel.redirect.GoToJieDianQian3PageHandler),
    (r"/activity/prize_go_jiedianqian_ht2", channel.redirect.GoToJieDianQianHT2PageHandler),
    (r"/activity/prize_go_xingxingqiandai1", channel.redirect.GoToXingXingQianDaiPageHandler),
    (r"/activity/prize_go_vipkid1", channel.redirect.GoToVipKidPageHandler),
    (r"/activity/prize_go_vipkid1_1", channel.redirect.GoToVipKid1_1PageHandler),
    (r"/activity/prize_go_vipkid1_2", channel.redirect.GoToVipKid1_2PageHandler),
    (r"/activity/prize_go_vipkid1_3", channel.redirect.GoToVipKid1_3PageHandler),
    (r"/activity/prize_go_huanleduobao_android1", channel.redirect.GoToHuanLeDuoBaoAndroidPageHandler),
    (r"/activity/prize_go_huanleduobao_ios1", channel.redirect.GoToHuanLeDuoBaoIOSPageHandler),
    (r"/activity/prize_go_mobai1", channel.redirect.GoToMoBaiPageHandler),
    (r"/activity/prize_go_guangdaka1", channel.redirect.GoToGuangDaKaPageHandler),
    (r"/activity/prize_go_luolizhajinhua1", channel.redirect.GoToLuoLiZhaJinHuaPageHandler),
    (r"/activity/prize_go_quanmama1", channel.redirect.GoToQuanMaMaPageHandler),
    (r"/activity/prize_go_quanmama2", channel.redirect.GoToQuanMaMa2PageHandler),
    (r"/activity/prize_go_yirendai1", channel.redirect.GoToYiRenDaiPageHandler),
    (r"/activity/prize_go_dazhongdianping1", channel.redirect.GoToDaZhongDianPingPageHandler),
    (r"/activity/prize_go_laicaicaipiao1", channel.redirect.GoToLaiCaiCaiPiaoPageHandler),
    (r"/activity/prize_go_xianjinxia1", channel.redirect.GoToXianJinXiaPageHandler),
    (r"/activity/prize_go_jinbeiqipai_android1", channel.redirect.GoToJinBeiQiPaiAndroidPageHandler),
    (r"/activity/prize_go_jinbeiqipai_ios1", channel.redirect.GoToJinBeiQiPaiIOSPageHandler),
    (r"/activity/prize_go_wanhaocaipiao1", channel.redirect.GoToWanHaoCaiPiaoPageHandler),
    (r"/activity/prize_go_wanhaocaipiao2", channel.redirect.GoToWanHaoCaiPiao2PageHandler),
    (r"/activity/prize_go_baoxinishoubiao1", channel.redirect.GoToBaoXiNiShouBiaoPageHandler),
    (r"/activity/prize_go_yinhezhixing1", channel.redirect.GoToYinHeZhiXingPageHandler),
    (r"/activity/prize_go_fopaiheiyaoshi1", channel.redirect.GoToFoPaiHeiYaoShiPageHandler),
    (r"/activity/prize_go_pixiu1", channel.redirect.GoToPiXiuPageHandler),
    (r"/activity/prize_go_yicaidao1", channel.redirect.GoToYiCaiDaoPageHandler),
    (r"/activity/prize_go_yicaidao_gxcdb1", channel.redirect.GoToGongXiangChongDianBaoYiCaiDaoPageHandler),
    (r"/activity/prize_go_paczxyk1", channel.redirect.GoToPingAnXinYongKaYDPageHandler),
    (r"/activity/prize_go_buyudashi1", channel.redirect.GoToBuYuDaShiPageHandler),
    (r"/activity/prize_go_koudaiauction_ios1", channel.redirect.GoToKouDaiAuctionIOSPageHandler),
    (r"/activity/prize_go_koudaiauction_android1", channel.redirect.GoToKouDaiAuctionAndroidPageHandler),
    (r"/activity/prize_go_huaerjie1", channel.redirect.GoToHuaErJiePageHandler),
    (r"/activity/prize_go_jinronghui1", channel.redirect.GoToJinRongHuiPageHandler),
    (r"/activity/prize_go_heiniudaikuan1", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/prize_go_heiniudaikuan2", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/prize_go_heiniudaikuan3", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/prize_go_heiniudaikuan4", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/prize_go_heiniudaikuan_lunbo", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/prize_go_heiniudaikuan_wowo", channel.redirect.GoToHeiNiuDaiKuanPageHandler),
    (r"/activity/prize_go_jinshancaipiao1", channel.redirect.GoToJinShanCaiPiaoPageHandler),
    (r"/activity/prize_go_kuaiyihua1", channel.redirect.GoToKuaiYiHuaPageHandler),
    (r"/activity/prize_go_taoxinwen1", channel.redirect.GoToTaoXinWenPageHandler),
    (r"/activity/prize_go_quanminduobao_ios1", channel.redirect.GoToQuanMingDuoBaoIOSPageHandler),
    (r"/activity/prize_go_quanminduobao_android1", channel.redirect.GoToQuanMingDuoBaoAndroidPageHandler),
    (r"/activity/prize_go_qiuqiudoudizhu1", channel.redirect.GoToQiuQiuDouDiZhuPageHandler),
    (r"/activity/prize_go_kuhuasuoping1", channel.redirect.GoToKuHuaSuoPingPageHandler),
    (r"/activity/prize_go_shanghaiyhxyk1", channel.redirect.GoToShangHaiYinHangXinYongKaPageHandler),
    (r"/activity/prize_go_leshua2", channel.redirect.GoToLeShua2PageHandler),
    (r"/activity/prize_go_leshua_out", channel.redirect.GoToLeShuaOutPageHandler),
    (r"/activity/prize_go_qianyoulu1", channel.redirect.GoToQianYouLuPageHandler),
    (r"/activity/prize_go_hulishajin1", channel.redirect.GoToHuLiShaJinPageHandler),
    (r"/activity/prize_go_heiyaoshi_pixiu1", channel.redirect.GoToHeiYaoShiPiXiuPageHandler),
    (r"/activity/prize_go_wonenglicai1", channel.redirect.GoToWoNengLiCaiPageHandler),
    (r"/activity/prize_go_heiniubaoxian1", channel.redirect.GoToHeiNiuBaoXianPageHandler),
    (r"/activity/prize_go_shandai1", channel.redirect.GoToShanDaiPageHandler),
    (r"/activity/prize_go_bingsineiku1", channel.redirect.GoToBingSiNeiKuPageHandler),
    (r"/activity/prize_go_T_shirtman1", channel.redirect.GoToTShirtManPageHandler),
    (r"/activity/prize_go_hengxinmetal1", channel.redirect.GoToHengXinMetalPageHandler),
    (r"/activity/prize_go_quanminauction_ios1", channel.redirect.GoToQuanMinAuctionPageHandler),
    (r"/activity/prize_go_quanminauction_android1", channel.redirect.GoToQuanMinAuctionPageHandler),
    (r"/activity/prize_go_koudaijc_ios1", channel.redirect.GoToKouDaiJingCaiIOSPageHandler),
    (r"/activity/prize_go_koudaijc_android1", channel.redirect.GoToKouDaiJingCaiAndroidPageHandler),
    (r"/activity/prize_go_wanrendoudizhu1", channel.redirect.GoToWanRenDouDiZhuPageHandler),
    (r"/activity/prize_go_wanrendoudizhu2", channel.redirect.GoToWanRenDouDiZhu2PageHandler),
    (r"/activity/prize_go_wanrendoudizhu_zp", channel.redirect.GoToWanRenDouDiZhuZPPageHandler),
    (r"/activity/prize_go_daishangqian1", channel.redirect.GoToDaiShangQianPageHandler),
    (r"/activity/prize_go_yiyuanduobao2_android", channel.redirect.GoToXYDuoBao2AndroidPageHandler),
    (r"/activity/prize_go_hengxinmetal1_zp", channel.redirect.GoToHengXingMetalZP1PageHandler),
    (r"/activity/prize_go_wangzherongyao1", channel.redirect.GoToWangZheRongYaoKaPageHandler),
    (r"/activity/prize_go_baoxiniqinglvbiao1", channel.redirect.GoToBaoXiNiQingLvBiaoPageHandler),
    (r"/activity/prize_go_tiantianzhajinhua1", channel.redirect.GoToTianTianZhaJinHuaPageHandler),
    (r"/activity/prize_go_tengxunlicaitong1", channel.redirect.GoToTengXunLiCaiTongPageHandler),
    (r"/activity/prize_go_xiangqiandai1", channel.redirect.GoToXiangQianDaiPageHandler),
    (r"/activity/prize_go_baidujinrong1", channel.redirect.GoToBaiDuJinRongPageHandler),
    (r"/activity/prize_go_360jietiao1", channel.redirect.GoTo360JieTiaoPageHandler),
    (r"/activity/prize_go_360jietiao_gxcdb1", channel.redirect.GoToGongXiangChongDianBao360JieTiaoPageHandler),
    (r"/activity/prize_go_yongqianbao1", channel.redirect.GoToYongQianBaoPageHandler),
    (r"/activity/prize_go_lvshoujianfei1", channel.redirect.GoToLvShouJianFeiPageHandler),
    (r"/activity/prize_go_binzhiheika1", channel.redirect.GoToBinZhiHeiKaPageHandler),
    (r"/activity/prize_go_dianwanchengzhajinhua1", channel.redirect.GoToDianWanChengZhaJinHuaPageHandler),
    (r"/activity/prize_go_songjiangdai1", channel.redirect.GoToSongJiangDaiPageHandler),
    (r"/activity/prize_go_kaixinqianbao1", channel.redirect.GoToKaiXinQianBaoPageHandler),
    (r"/activity/prize_go_kaniu1", channel.redirect.GoToKaNiuPageHandler),
    (r"/activity/prize_go_jiekuanzhuanjia1", channel.redirect.GoToJieKuanZhuanJiaPageHandler),
    (r"/activity/prize_go_yinghuangyule1", channel.redirect.GoToYingHuangYuLePageHandler),
    (r"/activity/prize_go_360daikuan1", channel.redirect.GoTo360DaiKuanPageHandler),
    (r"/activity/prize_go_51xinyongkaguanjia1", channel.redirect.GoTo51XinYongKaGuanJiaPageHandler),
    (r"/activity/prize_go_51xinyongkaguanjia2", channel.redirect.GoTo51XinYongKaGuanJia2PageHandler),
    (r"/activity/prize_go_51xinyongkaguanjia3", channel.redirect.GoTo51XinYongKaGuanJia3PageHandler),
    (r"/activity/prize_go_51xinyongkaguanjia_wowo1", channel.redirect.GoTo51XinYongKaGuanJiaWoWoPageHandler),
    (r"/activity/prize_go_niwodai1", channel.redirect.GoToNiWoDaiPageHandler),
    (r"/activity/prize_go_xianjindai1", channel.redirect.GoToXianJinDaiPageHandler),
    (r"/activity/prize_go_rong360_1", channel.redirect.GoToRong360PageHandler),
    (r"/activity/prize_go_rong360_zp", channel.redirect.GoToRong360ZPPageHandler),
    (r"/activity/prize_go_rong360_lunbo", channel.redirect.GoToRong360LunBoPageHandler),
    (r"/activity/prize_go_leshua3", channel.redirect.GoToLeShua3PageHandler),
    (r"/activity/prize_go_leshua_zp3", channel.redirect.GoToLeShuaZP3PageHandler),
    (r"/activity/prize_go_leshua_xq_zp3", channel.redirect.GoToLeShuaXiangQianZP3PageHandler),
    (r"/activity/prize_go_leshua_zp", channel.redirect.GoToLeShuaZPPageHandler),
    (r"/activity/prize_go_leshua_ht4", channel.redirect.GoToLeShuaHT4PageHandler),
    (r"/activity/prize_go_shandianpaimai1", channel.redirect.GoToShanDianPaiMaiPageHandler),
    (r"/activity/prize_go_wangyiguijinshu1", channel.redirect.GoToWangYiGuiJinShuPageHandler),
    (r"/activity/prize_go_mojie2", channel.redirect.GoToMoJie2PageHandler),
    (r"/activity/prize_go_xinerfu1", channel.redirect.GoToXinErFuPageHandler),
    (r"/activity/prize_go_tongchengyeyou1", channel.redirect.GoToTongChengYeYouPageHandler),
    (r"/activity/prize_go_360daikuan2", channel.redirect.GoTo360DaiKuan2PageHandler),
    (r"/activity/prize_go_fanliwang1", channel.redirect.GoToFanLiWangPageHandler),
    (r"/activity/prize_go_lanyueqipai1", channel.redirect.GoToLanYueQiPaiPageHandler),
    (r"/activity/prize_go_weijiaoyi1", channel.redirect.GoToWeiJiaoYiPageHandler),
    (r"/activity/prize_go_hnfopai1", channel.redirect.GoToHeiNiuFoPaiPageHandler),
    (r"/activity/prize_go_hnfopai2", channel.redirect.GoToHeiNiuFoPai2PageHandler),
    (r"/activity/prize_go_dingdangkuaiyao1", channel.redirect.GoToDingDangKuaiYaoPageHandler),
    (r"/activity/prize_go_shandianjiangjia1", channel.redirect.GoToShanDianJiangJiaPageHandler),
    (r"/activity/prize_go_boluodai1", channel.redirect.GoToJuJiuPeiPageHandler),
    (r"/activity/prize_go_zhuanqian1", channel.redirect.GoToZhuanQianPageHandler),
    (r"/activity/prize_go_daiba1", channel.redirect.GoToDaiBaPageHandler),
    (r"/activity/prize_go_daiba_ht1", channel.redirect.GoToDaiBaHT1PageHandler),
    (r"/activity/prize_go_dingguagua1", channel.redirect.GoToDingGuaGuaPageHandler),
    (r"/activity/prize_go_tuhaodayingjia1", channel.redirect.GoToTuHaoDaYingJiaPageHandler),
    (r"/activity/prize_go_xianjinjiekuan1", channel.redirect.GoToXianJinJieKuanPageHandler),
    (r"/activity/prize_go_pengboyule1", channel.redirect.GoToPengBoYuLePageHandler),
    (r"/activity/prize_go_zhaoshangka3", channel.redirect.GoToZhaoShangCredit3PageHandler),
    (r"/activity/prize_go_tiantianaicaipiao1", channel.redirect.GoToTianTianAiCaiPiaoPageHandler),
    (r"/activity/prize_go_tiantianaicaipiao_lj1", channel.redirect.GoToTianTianAiCaiPiaoLJPageHandler),
    (r"/activity/prize_go_tiantianaicaipiao_wt1", channel.redirect.GoToTianTianAiCaiPiaoWTZPPageHandler),
    (r"/activity/prize_go_tiantianaicaipiao_ht1", channel.redirect.GoToTianTianAiCaiPiaoHuiTuiPageHandler),
    (r"/activity/prize_go_tiantianaicaipiao_ios1", channel.redirect.GoToTianTianAiCaiPiaoIOSPageHandler),
    (r"/activity/prize_go_tiantianaicaipiao_ios_lj1", channel.redirect.GoToTianTianAiCaiPiaoIOSLJPageHandler),
    (r"/activity/prize_go_tiantianaicaipiao_ios_wt1", channel.redirect.GoToTianTianAiCaiPiaoIOSWTZPPageHandler),
    (r"/activity/prize_go_tiantianaicaipiao_ios_ht1", channel.redirect.GoToTianTianAiCaiPiaoIOSHuiTuiPageHandler),
    (r"/activity/prize_go_domwatch_f1", channel.redirect.GoToDomWatchFPageHandler),
    (r"/activity/prize_go_domwatch_m1", channel.redirect.GoToDomWatchMPageHandler),
    (r"/activity/prize_go_lingketixudao1", channel.redirect.GoToLingKeTiXuDaoageHandler),
    (r"/activity/prize_go_qiaohu1", channel.redirect.GoToQiaoHuPageHandler),
    (r"/activity/prize_go_mtwm1", channel.redirect.GoToMeiTuanWaiMaiPageHandler),
    (r"/activity/prize_go_xiangzhuanqian1", channel.redirect.GoToXiangZhuanQianPageHandler),
    (r"/activity/prize_go_kongtiaoshan1", channel.redirect.GoToKongTiaoShanPageHandler),
    (r"/activity/prize_go_dayangyule1", channel.redirect.GoToDaYangYuLePageHandler),
    (r"/activity/prize_go_laobanzhang1", channel.redirect.GoToLaoBanZhangPageHandler),
    (r"/activity/prize_go_fanliwang2", channel.redirect.GoToFanLiWang2PageHandler),
    (r"/activity/prize_go_hnpos1", channel.redirect.GoToHeiNiuPosPageHandler),
    (r"/activity/prize_go_tianmao1", channel.redirect.GoToTianMaoPageHandler),
    (r"/activity/prize_go_youjie1", channel.redirect.GoToYouJiePageHandler),
    (r"/activity/prize_go_youjie2", channel.redirect.GoToYouJie2PageHandler),
    (r"/activity/prize_go_youjie_ht1", channel.redirect.GoToYouJieHT1PageHandler),
    (r"/activity/prize_go_yinghuangguoji1", channel.redirect.GoToYingHuangGuoJiPageHandler),
    (r"/activity/prize_go_qianbaojinrong1", channel.redirect.GoToQianBaoJinRongPageHandler),
    (r"/activity/prize_go_baoxinishoubiao2", channel.redirect.GoToBaoXiNiShouBiao2PageHandler),
    (r"/activity/prize_go_baoxinishoubiao3", channel.redirect.GoToBaoXiNiShouBiao3PageHandler),
    (r"/activity/prize_go_baoxinishoubiao4", channel.redirect.GoToBaoXiNiShouBiao4PageHandler),
    (r"/activity/prize_go_baoxinishoubiao_ht2", channel.redirect.GoToBaoXiNiShouBiaoHT2PageHandler),
    (r"/activity/prize_go_baoxinishoubiao_ht3", channel.redirect.GoToBaoXiNiShouBiaoHT3PageHandler),
    (r"/activity/prize_go_baoxinishoubiao_wowo1", channel.redirect.GoToBaoXiNiShouBiaoWoWoPageHandler),
    (r"/activity/prize_go_baoxinishoubiao_lunbo2", channel.redirect.GoToBaoXiNiShouBiaoLunBoPageHandler),
    (r"/activity/prize_go_yuenanshajin1", channel.redirect.GoToYueNanShaJinPageHandler),
    (r"/activity/prize_go_dianwancheng1", channel.redirect.GoToDianWanChengPageHandler),
    (r"/activity/prize_go_dianwancheng_h5", channel.redirect.GoToDianWanChengH5PageHandler),
    (r"/activity/prize_go_jingpai1", channel.redirect.GoToJingPaiPageHandler),
    (r"/activity/prize_go_naixi1", channel.redirect.GoToNaiXiPageHandler),
    (r"/activity/prize_go_xiaobaojinrong1", channel.redirect.GoToXiaoBaoJinRongPageHandler),
    (r"/activity/prize_go_hnbaoxini1", channel.redirect.GoToHeiNiuBaoXiNiPageHandler),
    (r"/activity/prize_go_hnbaoxini_ht1", channel.redirect.GoToHeiNiuBaoXiNiPageHandler),
    (r"/activity/prize_go_chaodai1", channel.redirect.GoToChaoDaiPageHandler),
    (r"/activity/prize_go_shuisubei1", channel.redirect.GoToShuiSuBeiPageHandler),
    (r"/activity/prize_go_hualebei1", channel.redirect.GoToHuaLeBeiPageHandler),
    (r"/activity/prize_go_kuaishoucaipiao1", channel.redirect.GoToKuaiShouCaiPiaoPageHandler),
    (r"/activity/prize_go_baiyingqipai1", channel.redirect.GoToBaiYingQiPaiPageHandler),
    (r"/activity/prize_go_falaidihongjiu1", channel.redirect.GoToFaLaiDiHongJiuPageHandler),
    (r"/activity/prize_go_kuaishan1", channel.redirect.GoToKuaiShanPageHandler),
    (r"/activity/prize_go_tanwanqipai1", channel.redirect.GoToTanWanQiPaiPageHandler),
    (r"/activity/prize_go_nvshenliaotian1", channel.redirect.GoToNvShenLiaoTianPageHandler),
    (r"/activity/prize_go_niwojinrong1", channel.redirect.GoToNiWoJinRongPageHandler),
    (r"/activity/prize_go_niwojinrong_wowo1", channel.redirect.GoToNiWoJinRongPageHandler),
    (r"/activity/prize_go_kuaizhifu1", channel.redirect.GoToKuaiZhiFuPageHandler),
    (r"/activity/prize_go_jianzhiying1", channel.redirect.GoToJianZhiYingPageHandler),
    (r"/activity/prize_go_jieqiankuai1", channel.redirect.GoToJieQianKuaiPageHandler),
    (r"/activity/prize_go_huicheliandong1", channel.redirect.GoToHuiCheLianDongPageHandler),
    (r"/activity/prize_go_huicheliandong2", channel.redirect.GoToHuiCheLianDong2PageHandler),
    (r"/activity/prize_go_duoxiangjinhui1", channel.redirect.GoToDuoXiangJinHuiPageHandler),
    (r"/activity/prize_go_baolaiyule1", channel.redirect.GoToBaoLaiYuLePageHandler),
    (r"/activity/prize_go_baolaiyule2", channel.redirect.GoToBaoLaiYuLe2PageHandler),
    (r"/activity/prize_go_yingfuyingyu1", channel.redirect.GoToYingFuYingYuPageHandler),
    (r"/activity/prize_go_meifuquban1", channel.redirect.GoToMeiFuQuBanPageHandler),
    (r"/activity/prize_go_guizhoumaotai1", channel.redirect.GoToGuiZhouMaoTaiPageHandler),
    (r"/activity/prize_go_jiehuahua1", channel.redirect.GoToJieHuaHuaPageHandler),
    (r"/activity/prize_go_dalujietiao1", channel.redirect.GoToDaLuJieTiaoPageHandler),
    (r"/activity/prize_go_weilan2", channel.redirect.GoToWeiLan2PageHandler),
    (r"/activity/prize_go_niwojinrong2", channel.redirect.GoToNiWoJiRong2PageHandler),
    (r"/activity/prize_go_zihan1", channel.redirect.GoToZiHanPageHandler),
    (r"/activity/prize_go_jiqianjingying1", channel.redirect.GoToJiQianJingYingPageHandler),
    (r"/activity/prize_go_haijiadianwan1", channel.redirect.GoToHaiJiaDianWanPageHandler),
    (r"/activity/prize_go_feikejinbei1", channel.redirect.GoToFeiKeJinBeiPageHandler),
    (r"/activity/prize_go_shanyin1", channel.redirect.GoToShanYinPageHandler),
    (r"/activity/prize_go_yundingyule1", channel.redirect.GoToYunDingYuLePageHandler),
    (r"/activity/prize_go_faguoXO1", channel.redirect.GoToFaGuoXOPageHandler),
    (r"/activity/prize_go_linwang1", channel.redirect.GoToLinWangPageHandler),
    (r"/activity/prize_go_fangnanke1", channel.redirect.GoToFangNanKePageHandler),
    (r"/activity/prize_go_hrbfopai1", channel.redirect.GoToHaErBinPageHandler),
    (r"/activity/prize_go_zhinengbiao1", channel.redirect.GoToZhiNengBiaoPageHandler),
    (r"/activity/prize_go_weisikaibiao1", channel.redirect.GoToWeiSiKaiBiaoPageHandler),
    (r"/activity/prize_go_doumengshajin1", channel.redirect.GoToDouMengShaJinPageHandler),
    (r"/activity/prize_go_wacaixinyongka1", channel.redirect.GoToWaCaiXinYongKaPageHandler),
    (r"/activity/prize_go_boniuyouxi1", channel.redirect.GoToBoNiuYouXiPageHandler),
    (r"/activity/prize_go_heiniuyouqian1", channel.redirect.GoToHeiNiuYouQianPageHandler),
    (r"/activity/prize_go_heiniuyouqian2", channel.redirect.GoToHeiNiuYouQianPageHandler),
    (r"/activity/prize_go_heiniuyouqian3", channel.redirect.GoToHeiNiuYouQianPageHandler),
    (r"/activity/prize_go_mianfeisongjianfei1", channel.redirect.GoToMianFeiSongJianFeiPageHandler),
    (r"/activity/prize_go_tubatu1", channel.redirect.GoToTuBaTuPageHandler),
    (r"/activity/prize_go_chuangyibiao1", channel.redirect.GoToChuangYiBiaoPageHandler),
    (r"/activity/prize_go_jikaicai1", channel.redirect.GoToJiKaiCaiPageHandler),
    (r"/activity/prize_go_dezhoupuke1", channel.redirect.GoToDeZhouPuKePageHandler),
    (r"/activity/prize_go_zhongyicaipiao_trans1", channel.redirect.GoToZhongYiCaiPiaoPageHandler),
    (r"/activity/prize_go_zhuoyicaipiao_trans1", channel.redirect.GoToZhuoYiCaiPiaoPageHandler),
    (r"/activity/prize_go_shoujizhuan1", channel.redirect.GoToShouJiZhuanPageHandler),
    (r"/activity/prize_go_cixuanfu1", channel.redirect.GoToCiXuanFuPageHandler),
    (r"/activity/prize_go_ajiejianfei1", channel.redirect.GoToAJieJianFeiPageHandler),
    (r"/activity/prize_go_weilan3", channel.redirect.GoToWeiLanQiPai3PageHandler),
    (r"/activity/prize_go_daguangzongwangzhuan1", channel.redirect.GoToDaGuangZongWangZhuanPageHandler),
    (r"/activity/prize_go_zhangshangaomen1", channel.redirect.GoToZhangShangAoMenPageHandler),
    (r"/activity/prize_go_wangzhechuanqi1", channel.redirect.GoToWangZheChuanQiPageHandler),
    (r"/activity/prize_go_laosibinbiao1", channel.redirect.GoToLaoSiBinBiaoPageHandler),
    (r"/activity/prize_go_anzongwangzhuan1", channel.redirect.GoToAnZongWangZhuanPageHandler),
    (r"/activity/prize_go_liuzongwangzhuan1", channel.redirect.GoToLiuZongWangZhuanPageHandler),
    (r"/activity/prize_go_yanzongsongjianfei1", channel.redirect.GoToYanZongSongJianFeiPageHandler),
    (r"/activity/prize_go_shenwangzhuan1", channel.redirect.GoToShenWangZhuanPageHandler),
    (r"/activity/prize_go_kuaiquzhuanqian1", channel.redirect.GoToKuaiQuZhuanQianPageHandler),
    (r"/activity/prize_go_mashangzhuanqian1", channel.redirect.GoToMaShangZhuanQianPageHandler),
    (r"/activity/prize_go_aiqiyibaoxian1", channel.redirect.GoToAiQiYiBaoXianPageHandler),
    (r"/activity/prize_go_jianzhizhuan1", channel.redirect.GoToJianZhiZhuanPageHandler),
    (r"/activity/prize_go_xingyuncaipiao1", channel.redirect.GoToXingYunCaiPiaoPageHandler),
    (r"/activity/prize_go_mamabang1", channel.redirect.GoToMaMaBangPageHandler),
    (r"/activity/prize_go_youhaoya1", channel.redirect.GoToYouHaoYaPageHandler),
    (r"/activity/prize_go_yunhaoqipai1", channel.redirect.GoToYunHaoQiPaiPageHandler),

    # 掌游4金贝棋牌
    (r"/activity/prize_go_zy4_jinbeiqipai_android1", channel.redirect.GoToZYJinBeiQiPaiAndroidPageHandler),
    (r"/activity/prize_go_zy4_jinbeiqipai_ios1", channel.redirect.GoToJinBeiQiPaiIOSPageHandler),


    # 转盘推广链接
    # 去哪儿
    (r"/activity/qunaer_prize1", channel.redirect.QuNaErPrizePageHandler),
    # 网氪
    (r"/activity/wangke_prize1", channel.redirect.WangKePrizePageHandler),
    (r"/activity/wangke_prize2", channel.redirect.WangKePrize2PageHandler),
    # hlwifi
    (r"/activity/hlwifi_prize1", channel.redirect.HLWifiPrizePageHandler),
    (r"/activity/hlwifi_prize2", channel.redirect.HLWifiPrize2PageHandler),
    (r"/activity/hlwifi_prize3", channel.redirect.HLWifiPrize3PageHandler),
    (r"/activity/hlwifi_prize4", channel.redirect.HLWifiPrize4PageHandler),
    (r"/activity/hlwifi_prize5", channel.redirect.HLWifiPrize5PageHandler),
    (r"/activity/hlwifi_prize6", channel.redirect.HLWifiPrize6PageHandler),
    # 掌游
    (r"/activity/zhangyou_prize1", channel.redirect.ZhangYouPrizePageHandler),
    (r"/activity/zhangyou_prize2", channel.redirect.ZhangYouPrize2PageHandler),
    (r"/activity/zhangyou_prize3", channel.redirect.ZhangYouPrize3PageHandler),
    (r"/activity/zhangyou_prize4", channel.redirect.ZhangYouPrize4PageHandler),
    (r"/activity/zhangyou_prize5", channel.redirect.ZhangYouPrize5PageHandler),
    # 赢纳
    (r"/activity/yingna_prize1", channel.redirect.YingNaPrizePageHandler),
    # 兴吾通
    (r"/activity/xingwutong_prize1", channel.redirect.XingWuTongPrizePageHandler),
    # wuli
    (r"/activity/wuli_prize1", channel.redirect.WuLiPrizePageHandler),
    # 众智
    # (r"/activity/zhongzhi_prize1", channel.redirect.ZhongZhiPrizePageHandler),
    # (r"/activity/zhongzhi_prize2", channel.redirect.ZhongZhiPrize2PageHandler),
    # (r"/activity/zhongzhi_prize3", channel.redirect.ZhongZhiPrize3PageHandler),
    # 照片打印
    (r"/activity/zhaopiandayin_prize1", channel.redirect.ZhaoPianDaYinPrizePageHandler),
    (r"/activity/zhaopiandayin_prize2", channel.redirect.ZhaoPianDaYinPrize2PageHandler),
    (r"/activity/zhaopiandayin_prize3", channel.redirect.ZhaoPianDaYinPrize3PageHandler),
    # 天创
    (r"/activity/tianchuang_prize1", channel.redirect.TianChuangPrizePageHandler),
    # 网氪公交
    (r"/activity/wkgongjiao1", channel.tv_yaoyiyao.WangKeGongJiaoPage1Handler),
    # 糗事百科
    (r"/activity/qiushi_prize1", channel.redirect.QiuShiBaiKePrizePageHandler),
    # 快友
    (r"/activity/adview_prize1", channel.redirect.KuaiYouPrizePageHandler),
    (r"/activity/adview_prize2", channel.redirect.KuaiYouPrize2PageHandler),
    (r"/activity/adview_prize3", channel.redirect.KuaiYouPrize3PageHandler),
    (r"/activity/adview_prize4", channel.redirect.KuaiYouPrize4PageHandler),
    (r"/activity/adview_prize5", channel.redirect.KuaiYouPrize5PageHandler),
    # 光微科技
    (r"/activity/gwkj_prize1", channel.redirect.GuangWeiKeJiPrizePageHandler),
    # 享钱微信支付
    (r"/activity/xiangqwxzf_prize1", channel.redirect.XiangQianWeiXinZhiFuPrizePageHandler),
    # 电影
    (r"/activity/dianying_prize1", channel.redirect.DianYingPrizePageHandler),
    # 讯飞
    (r"/activity/xunfei_prize1", channel.redirect.XunFeiPrizePageHandler),
    # 讯飞黑色
    (r"/activity/xunfei_prize2", channel.redirect.XunFeiPrize2PageHandler),
    # 讯飞 砸蛋2
    (r"/activity/xunfei_egg2", insurance.lottery.egg.XunFeiEgg2BasePageHandler),
    # 51福利网
    (r"/activity/51fuliwang_prize1", channel.redirect.FuLiWang51PrizePageHandler),
    # 运营商
    (r"/activity/yys_prize1", channel.redirect.YunYinShangPrizePageHandler),
    # 窝窝支付
    (r"/activity/wowo_prize1", channel.redirect.WoWoPrizePageHandler),
    # 共享充电宝
    (r"/activity/gxcdb_prize1", channel.redirect.GongXiangChongDianBaoPrizePageHandler),
    # 爱奇艺
    (r"/activity/aqyddcpc1", channel.redirect.AiQiYiPrizePageHandler),

    # 黑色推广转盘
    (r"/activity/test_prize1", channel.redirect.TuiGuangPrizePageHandler),
    # # 掌游
    # (r"/activity/zhangyou_prize1", channel.redirect.ZhangYouPrizeNewPageHandler),
    # (r"/activity/zhangyou_prize2", channel.redirect.ZhangYouPrize2NewPageHandler),
    # (r"/activity/zhangyou_prize3", channel.redirect.ZhangYouPrize3NewPageHandler),
    # (r"/activity/zhangyou_prize4", channel.redirect.ZhangYouPrize4NewPageHandler),
    (r"/activity/zhangyou_egg4", insurance.lottery.egg.ZhangYou4EggBasePageHandler),
    # # 众智
    (r"/activity/zhongzhi_prize1", channel.redirect.ZhongZhiPrizeNewPageHandler),
    (r"/activity/zhongzhi_prize2", channel.redirect.ZhongZhiPrize2NewPageHandler),
    (r"/activity/zhongzhi_prize3", channel.redirect.ZhongZhiPrize3NewPageHandler),
    # PPTV
    (r"/activity/pptv_prize1", channel.redirect.PPTVPrizePageHandler),
    # 申米
    (r"/activity/shenmi_prize1", channel.redirect.ShenMiPrizePageHandler),
    # 浩闪
    (r"/activity/haoshan_prize1", channel.redirect.HaoShanPrizePageHandler),
    # 融臻
    (r"/activity/rongzhen_prize1", channel.redirect.RongZhenPrizePageHandler),
    # 小支
    (r"/activity/xiaozhi_prize1", channel.redirect.XiaoZhiPrizePageHandler),


    # 北大荒定制转盘
    (r"/activity/bdh_prize1", channel.redirect.BeiDaHuangPrizePageHandler),
    (r"/activity/bdh_prize_interface1", channel.redirect.BeiDaHuangPrizeInterfaceHandler),
    (r"/activity/bdh_my_prizes_interface1", channel.redirect.BeiDaHuangMyPrizesInterfaceHandler),

    # 微信公众号接口
    (r"/weixin/validate", weixin.wxhandler.ValidateHandler),
    (r"/weixin/validate_local_test", weixin.wxhandler.ValidateHandler),
    (r"/weixin/api/person/info", weixin.wxhandler.UserInfoHandler),
    (r"/weixin/api/login/passport", weixin.wxhandler.LoginHandler),
    (r"/weixin/api/insurance/list", weixin.wxhandler.InsuranceListInfoHandler),
    (r"/weixin/api/insurance/calculate", weixin.wxhandler.InsuranceCalculateHandler),
    (r"/weixin/api/captcha/token/generator", weixin.wxhandler.GenCaptchaPhoneRandomHandler),
    (r"/weixin/api/policy/searcher", weixin.wxhandler.PolicyInfoSearcherHandler),
    (r"/weixin/api/policy/list", weixin.wxhandler.WeixinPolicyInfoListHandler),
    (r"/weixin/api/policy/detail", weixin.wxhandler.WeixinPolicyInfoDetailHandler),
    (r"/weixin/api/fulishe/info", weixin.wxhandler.WeixinFulisheUrlHandler),
    (r"/weixin/menu_setter", weixin.wxhandler.MenuHandler),
    (r"/weixin/home", weixin.wxhandler.WeixinHomeHandler),
    (r"/weixin/getsign", weixin.wxhandler.SignatureHandler),
    (r"/weixin/insurance", weixin.insurance_wx.InsuranceBaseHandler),

    (r'/MP_verify_WrWHIIfGnweVgknE.txt', weixin.wxhandler.VerifyDomainHandler),
    # 微信泰康测保
    (r"/activity/weixin_calculate_taikang", channel.calculate_taikang.WeiXinCalculatePremiumTaiKang),

    # 朗阁考试报名测试
    (r"/activity/langge", channel.langge.LangGeWaiYuPeiXunBaoMingPageHandler),

    # 福利社抽奖综合页
    (r"/activity/carnival", insurance.lottery.carnival.CarnivalPageHandler),
    (r"/activity_mgb/carnival", insurance.lottery.carnival.CarnivalPageHandler),
    # 刮券活动
    (r"/activity/scratch_ticket", insurance.lottery.guaquan.ScratchTicketBasePageHandler),
    (r"/activity_mgb/scratch_ticket", insurance.lottery.guaquan.ScratchTicketBasePageHandler),
    # 拆礼物活动
    (r"/activity/open_gift", insurance.lottery.chailiwu.ChaiLiWuPageHandler),
    (r"/activity_mgb/open_gift", insurance.lottery.chailiwu.ChaiLiWuPageHandler),
    # 挖金币活动
    (r"/activity/dig_gold", insurance.lottery.wabao.DigGoldBasePageHandler),
    (r"/activity_mgb/dig_gold", insurance.lottery.wabao.DigGoldBasePageHandler),
    # 砸蛋
    (r"/activity/smash_egg", insurance.lottery.egg.SmashEggBasePageHandler),
    (r"/activity_mgb/smash_egg", insurance.lottery.egg.SmashEggBasePageHandler),
    (r"/activity/smash_egg_new", insurance.lottery.egg.SmashEggBackBlockBasePageHandler),
    (r"/activity_mgb/smash_egg_new", insurance.lottery.egg.SmashEggBackBlockBasePageHandler),

    (r"/activity/pick_prize", insurance.lottery.pick.SmashEggPickHandler),
    (r"/activity_mgb/pick_prize", insurance.lottery.pick.SmashEggPickHandler),
    (r"/activity/extra_activity", insurance.lottery.pick.ExtraActivityHandler),
    (r"/activity_mgb/extra_activity", insurance.lottery.pick.ExtraActivityHandler),

    # 新红包弹窗
    (r"/activity/red_packet_pick", insurance.lottery.red_packet.RedPacketPickHandler),
    (r"/activity_mgb/red_packet_pick", insurance.lottery.red_packet.RedPacketPickHandler),

    # ----------------------------------------------  商城  --------------------------------------------------

    # 佛牌
    (r"/shop/fopai1", shop.jingpin_shop.FoPaiShopPageHandler),
    (r"/shop/fopai2", shop.jingpin_shop.FoPai2ShopPageHandler),
    (r"/shop/jrtt_fp1", shop.jingpin_shop.JinRiTouTiaoFoPaiShopPageHandler),
    (r"/shop/select_interface", shop.jingpin_shop.FoPaiSelectInterface),
    (r"/shop/fopai_select_interface", shop.jingpin_shop.FoPaiSelect2Interface),

    # 多姆表
    (r"/shop/watch_f1", shop.jingpin_shop.FemaleWatchShopPageHandler),
    (r"/shop/watch_m1", shop.jingpin_shop.MaleWatchShopPageHandler),
    (r"/shop/select_watch", shop.jingpin_shop.WatchSelectInterface),

    # 堡希尼
    (r"/shop/baoxini1", shop.jingpin_shop.BaoXiNiShopPageHandler),
    (r"/shop/baoxini2", shop.jingpin_shop.BaiChuanBaoXiNiShopPageHandler),
    (r"/shop/baoxini_select_interface", shop.jingpin_shop.BaoXiNiSelectInterface),

    # 威斯凯表
    (r"/shop/weisikai1", shop.jingpin_shop.WeiSiKaiShopPageHandler),

    # pos机
    # (r"/shop/pos1", shop.jingpin_shop.PosShopPageHandler),
    # (r"/shop/pos2", shop.jingpin_shop.Pos38ShopPageHandler),
    (r"/shop/hnbflmpos1", shop.jingpin_shop.PosShopPageHandler),
    (r"/shop/hnbflmpos2", shop.jingpin_shop.Pos38ShopPageHandler),

    (r"/test_jump", page_base.TestRedirectPageHandler),

    # ----------------------------------------------  接口  --------------------------------------------------

    (r"/shop/cixuanfu1", channel.cixuanfu.CiXuanFuPageHandler),
    (r"/shop/youhaoya1", channel.youhaoya.YouHaoYaPageHandler),
    
    #测试
	
	# ----------------------------------------------  微信，黑牛有钱  -----------------------------------------
    (r"/weinxin/loan/validate", weixin.loan.loan_handlers.ValidateHandler),
    (r"/weixin/loan/menu_setter", weixin.loan.loan_handlers.MenuHandler),
    (r"/weixin/loan/api/login/passport", weixin.loan.loan_handlers.LoginHandler),
    (r"/weixin/loan/api/random", weixin.loan.loan_handlers.RandomHandler),
    (r"/weixin/loan/api/captcha", weixin.loan.loan_handlers.CatpchaHandler),
    (r"/weixin/loan/api/captchacheck", weixin.loan.loan_handlers.CatpchaCheckHandler),
    (r"/weixin/loan/api/bind", weixin.loan.loan_handlers.BindHandler),
    (r"/weixin/loan/api/modify_mobile", weixin.loan.loan_handlers.ModifyMobileHandler),
    (r"/weixin/loan/api/bindcheck", weixin.loan.loan_handlers.BindCheckHandler),
    (r"/weixin/loan/api/float_ad", weixin.loan.loan_handlers.LoanHomeFloatAdHandler),
    (r"/weixin/loan/api/home", weixin.loan.loan_handlers.LoanInitApiHandler),
    (r"/weixin/loan/api/evaluate/financing", weixin.loan.loan_handlers.LoanCheckQuestionApiHandler),
    (r"/weixin/loan/api/question", weixin.loan.loan_handlers.LoanQuestionApiHandler),
    (r"/weixin/loan/api/financing_result", weixin.loan.loan_handlers.LoanQuestionResultApiHandler),
    (r"/weixin/loan/api/list/loan", weixin.loan.loan_handlers.LoanListApiHandler),
    (r"/weixin/loan/api/list/financing", weixin.loan.loan_handlers.FinancingListApiHandler),
    (r"/weixin/loan/api/list/insu", weixin.loan.loan_handlers.InsuranceListApiHandler),
    (r"/weixin/loan/api/list/insu/detail", weixin.loan.loan_handlers.InsuranceDetailApiHandler),
    (r"/weixin/loan/api/evaluate/loan", weixin.loan.loan_handlers.LoanCheckRecordApiHandler),
    (r"/weixin/loan/api/fillin", weixin.loan.loan_handlers.LoanFillinApiHandler),
    (r"/weixin/loan/api/perfected", weixin.loan.loan_handlers.LoanPerfectedApiHandler),
    (r"/weixin/loan/api/big_loan", weixin.loan.loan_handlers.LoanLargeRecommendApiHandler),
    (r"/weixin/loan/api/big_loan_check", weixin.loan.loan_handlers.LoanLargeCheckApiHandler),
    (r"/weixin/loan/api/small_loan", weixin.loan.loan_handlers.LoanSmallRecommendApiHandler),
    (r"/weixin/loan/api/loan_result", weixin.loan.loan_handlers.LoanResultApiHandler),
    (r"/weixin/loan/api/mine", weixin.loan.loan_handlers.LoanMineApiHandler),
    (r"/weixin/loan/api/personal/message", weixin.loan.loan_handlers.LoanPersonalMsgApiHandler),
    (r"/weixin/loan/api/personal/loan", weixin.loan.loan_handlers.LoanPersonalLoanApiHandler),
    (r"/weixin/loan/api/personal/policy", weixin.loan.loan_handlers.LoanMyPolicyApiHandler),
    (r"/weixin/loan/api/personal/policy_detail", weixin.loan.loan_handlers.LoanMyPolicyDetailApiHandler),
    (r"/weixin/loan/api/personal/policy_select", weixin.loan.loan_handlers.LoanOthersPolicyDetailApiHandler),
    (r"/weixin/loan/api/insu", weixin.loan.loan_handlers.InsuCalculateHandler),
    (r"/weixin/loan/api/tool/lottery", weixin.loan.loan_handlers.LotteryHandler),
    (r"/weixin/loan/api/tool/salary", weixin.loan.loan_handlers.SalaryHandler),
    (r"/weixin/loan/api/tool/salary_sociaty", weixin.loan.loan_handlers.SalarySociatyHandler),
    (r"/weixin/loan/api/tool/result_salary", weixin.loan.loan_handlers.SalaryResultHandler),
    (r"/weixin/loan/api/info/list", weixin.loan.loan_handlers.PageListHandler),
    (r"/weixin/loan/api/info/content", weixin.loan.loan_handlers.PageContentHandler),
    
    (r"/weixin/loan/views/auth/(.+)", weixin.loan.loan_handlers.LoanViewsAuthPageHandler),
    (r"/weixin/loan/views/bind/(.+)", weixin.loan.loan_handlers.LoanViewsBindPageHandler),
    (r'/MP_verify_msVousXb68LpeIzK.txt', weixin.loan.loan_handlers.VerifyDomainHandler),
    
    (r'/activity/weixin/sudaizhijia', weixin.loan.loan_handlers.SuDaiZhiJiaPageHandler),
    (r'/activity/weixin/rong360', weixin.loan.loan_handlers.Rong360PageHandler),
    (r'/activity/weixin/paph', weixin.loan.loan_handlers.PingAnPuHuiPageHandler),
    (r'/activity/weixin/heika', weixin.loan.loan_handlers.HeikaPageHandler),
    (r'/activity/weixin/huicheliandong', weixin.loan.loan_handlers.HuiCheLianDongPageHandler),
    (r'/activity/weixin/dalujietiao', weixin.loan.loan_handlers.DaLuJieTiaoPageHandler),
    (r'/activity/weixin/niwodai', weixin.loan.loan_handlers.NiWoDaiPageHandler),
    
    (r'/weixin/loan/api/tool/mortgage', weixin.loan.loan_handlers.MortgagePageHandler),
    (r'/weixin/loan/api/tool/result_mortgage', weixin.loan.loan_handlers.MortgageResultPageHandler),
    (r'/weixin/loan/api/ad/ticket', weixin.loan.loan_handlers.AdPageHandler)
]



