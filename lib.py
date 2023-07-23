import requests,json,random
import uuid,re,os,sys
from bs4 import BeautifulSoup
class Api_Facebook_Profile:
	def __init__(self)->None:
		pass
	def get_thongtin(self):
		self.headers={'authority':'mbasic.facebook.com','cache-control':'max-age=0','sec-ch-ua':'"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','upgrade-insecure-requests':'1','origin':'https://mbasic.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site':'same-origin','sec-fetch-mode':'navigate','sec-fetch-user':'?1','sec-fetch-dest':'document','referer':'https://mbasic.facebook.com/','accept-language':'en-US,en;q=0.9','cookie':self.cookie}
		try:
			home=requests.get('https://mbasic.facebook.com/profile.php',headers=self.headers).text
			self.fb_dtsg=home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
			self.jazoest=home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
			ten=home.split('<title>')[1].split('</title>')[0]
			self.user_id=self.cookie.split('c_user=')[1].split(';')[0]
			return ten,self.user_id
		except:
			return False
	def regpage(self):
		ho=random.choice(['Huỳnh','Đào','Ngô','Võ','Vũ','Đặng','Hàn','Trần','Hoàng','Quyền','Kiều','Bạch','Trịnh','Phạm','Trang','Lý','Lê','Ân','Dữu','Giang','Bành','Đỗ','Thân','Phan','Nguyễn','Thủy','Tống','Chu','Dương','Bùi','Hồ','Trầm','Quách','Quang','Mã','Kim','Lạc','Uất','Nghiêm','Úc','Thạch','Phí','Diệp','Thảo','Lục','Thi','Vĩnh','Ngư','Vưu','Hà','Lâm','Đoàn','Liễu','Phùng','La','Mạc','Đàm','Cao','Phó','Triệu','Vương','Tôn','Đinh','Chử','Trương','Tiêu','Tô','An','Châu','Văn','Mạch']);dem=random.choice(['Mộng','Diễm','Bích','Tâm','Hương','Việt','Lan','Hạnh','Nguyệt','Bảo','Ngọc','Mỹ','Hoa','Tịnh','Thùy','Thu','Thụy','Thiên','Phương','Giang','Trang','Nhã','Kim','Diệu','Huyền','An','Mai','Quế','Trúc','Tú','Thái','Lệ','Triều','Minh','Thanh','Xuân','Quỳnh','Khánh','Nhật','Hồng','Anh','Hải','Thúy','Ðông','Ánh','Tuyết','Thảo','Bội','Dạ','Thiện','Bạch','Linh','Cẩm','Thục','Thi','Kiều','Hoài','Hà','Phượng','Huệ','Yến','Thủy','Hoàn','Vũ','Uyển','Lê','Nguyên','Lưu','Lam','Hoàng','Vân','Sương','Như','Trà','Ban','Tuệ','Gia','Chi'])
		self.name_page=ho+' '+dem+' '+random.choice(['Nguyệt','Thảo','Nguyên','Thủy','Hà','Vy','Phương','Khuê','Mai','Uyển','Nga','Tiên','Trúc','Oanh','Yến','Thiên','Lâm','Dung','Sương','Uyên','Liên','Như','Lam','Trâm','Vân','Anh','Trang','Thanh','Nhã','Hương','Phượng','Hằng','Ngọc','Nhàn','Khôi','Linh','Quỳnh','Trà','Trinh','Yên','Khanh','Hiền','Loan','Nhi','My','Ánh','Sa','Thoa','Hậu','Kiều','Tuyền','Xuyến','Lan','Thúy','Thu','Quyên','Quế','An','Giang','Chi','Châu','Hòa','Tuyết','Phúc','Hạnh','Ðào','Hoa','Xuân','Thương','Hợp','Hồng','Minh','San','Ðiệp','Ly','Diệp','Vi','Diễm','Trân','Nghi','Ngà','Thắm','Ân','Khánh','Hường','Huệ','Thư','Huyền','Băng','Giao','Quân','Ngân','Ái','Mẫn','Bình','Bảo','Tú','Nương'])
		headers={'authority':'www.facebook.com','accept':'*/*','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','origin':'https://www.facebook.com','referer':'https://www.facebook.com/pages/creation/?ref_type=launch_point','sec-ch-prefers-color-scheme':'light','sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','viewport-width':'1221','x-fb-friendly-name':'AdditionalProfilePlusCreationMutation','x-fb-lsd':'wPd4PRo0e2MNyiZJhrq96a','cookie':self.cookie,}
		data={'av':self.user_id,'fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'AdditionalProfilePlusCreationMutation','variables':'{"input":{"bio":"categories","categories":["660696964377118"],"creation_source":"comet","name":"'+self.name_page+'","page_referrer":"launch_point","actor_id":"'+self.user_id+'","client_mutation_id":"1"}}','server_timestamps':'true','doc_id':'5903223909690825',}
		try:
			response=requests.post('https://www.facebook.com/api/graphql/',headers=headers,data=data)
			if '"id":' in response.text:
				self.id_page=response.json()['data']['additional_profile_plus_create']['additional_profile']['id']
				return True
			else:
				return False 
		except:
			return False 
	def upavt(self):
		id=random.choice(['226990999962252','226990879962264','226990453295640','226990666628952'])
		ck_pro5=self.cookie+'; i_user='+self.id_page+';'
		headers={'authority':'www.facebook.com','accept':'*/*','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':ck_pro5,'origin':'https://www.facebook.com','referer':'https://www.facebook.com/'+self.id_page,'sec-ch-prefers-color-scheme':'dark','sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','viewport-width':'979','x-fb-friendly-name':'AdditionalProfilePlusCreationMutation','x-fb-lsd':'ZM7FAk6cuRcUp3imwqvHTY','viewport-width':'1366',}
		data={'av':self.id_page,'fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'variables':'{"input":{"attribution_id_v2":"CometPhotoRoot.react,comet.mediaviewer.photo,via_cold_start,1689257246572,247308,,","caption":"","existing_photo_id":"'+id+'","expiration_time":null,"profile_id":"'+self.id_page+'","profile_pic_method":"EXISTING","profile_pic_source":"PHOTO_VIEW","scaled_crop_rect":{"height":1,"width":1,"x":0,"y":0},"skip_cropping":true,"actor_id":"'+self.id_page+'","client_mutation_id":"1"},"isPage":false,"isProfile":true,"sectionToken":"UNKNOWN","collectionToken":"UNKNOWN","scale":2}','server_timestamps':'true','doc_id':'6041079162654149',}
		try:
			response=requests.post('https://www.facebook.com/api/graphql/',headers=headers,data=data).text
			self.id_avt=response.split('"profilePhoto":{')[1].split('},"id":"')[1].split('"}')[0]
			return self.id_page in response
		except:
			return False
	def upbia(self):
		ck_pro5=self.cookie+'; i_user='+self.id_page+';'
		data={'av':self.id_page,'fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'ProfileCometCoverPhotoUpdateMutation','variables':'{"input":{"attribution_id_v2":"CometPhotoRoot.react,comet.mediaviewer.photo,unexpected,1684058187148,900492,,;ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1684058178238,428791,190055527696468,69#15#301","cover_photo_id":"'+self.id_avt+'","focus":{"x":0.5,"y":0.500170998632011},"target_user_id":"'+self.id_page+'","actor_id":"'+self.id_page+'","client_mutation_id":"1"},"scale":2,"contextualProfileContext":null}','server_timestamps':'true','doc_id':'6099517113440760'}
		headers={'Host':'www.facebook.com','sec-ch-ua':'"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','viewport-width':'980','x-fb-friendly-name':'ProfileCometCoverPhotoUpdateMutation','x-fb-lsd':'I-zYUFEcjyfhCgpsalT5IQ','sec-ch-ua-platform-version':'""','content-type':'application/x-www-form-urlencoded','x-asbd-id':'198387','sec-ch-ua-full-version-list':'"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-prefers-color-scheme':'dark','sec-ch-ua-platform':'"Linux"','accept':'*/*','origin':'https://www.facebook.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.facebook.com/'+self.id_page,'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':ck_pro5}
		try:
			response=requests.post('https://www.facebook.com/api/graphql/',headers=headers,data=data).text
			return self.id_page in response
		except:
			return False
	def get_pro5(self):
		headers={'authority':'www.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language':'vi',
		               'cookie':self.cookie,
		               'sec-ch-prefers-color-scheme':'light',
		               'sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
		               'sec-ch-ua-mobile':'?0',
		               'sec-ch-ua-platform':'"Windows"',
		               'sec-fetch-dest':'document',
		               'sec-fetch-mode':'navigate',
		               'sec-fetch-site':'none',
		               'sec-fetch-user':'?1',
		               'upgrade-insecure-requests':'1',
		               'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
		               'viewport-width':'1366',
		}
		data={
		   'av':self.user_id,
		   'fb_dtsg':self.fb_dtsg,
		   'jazoest':self.jazoest,
		   'fb_api_caller_class':'RelayModern',
		   'fb_api_req_friendly_name':'CometSettingsDropdownListQuery',
		   'variables':'{"fetchTestUserProfileListCell":false,"includeHorizBadging":false,"inProfileSwitcherEntry":false,"inSimpleHeaderEntry":true,"scale":2}',
		   'server_timestamps':'true',
		   'doc_id':'8179507702122101',
		}
		try:
			a=requests.post('https://www.facebook.com/api/graphql/',headers=headers,data=data).json()
			get=a['data']['viewer']['actor']['profile_switcher_eligible_profiles']
			tong=get['count']
			data=get['nodes']
			return tong,data
		except:
			return False
	def get_post(self,id):
		cookie=self.cookie
		headers={'Host':'www.facebook.com','cache-control':'max-age=0','viewport-width':'980','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Linux"','sec-ch-prefers-color-scheme':'dark','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site':'same-origin','sec-fetch-mode':'navigate','sec-fetch-user':'?1','sec-fetch-dest':'document','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':cookie}
		try:
			self.url=requests.get('https://www.facebook.com/'+id,headers=headers).url
			home=requests.get(self.url,headers=headers).text
			if '/videos/' in self.url:
				feedback_id=home.split('"feedback":{"id":"')[1].split('"')[0]
			else:
				feedback_id=home.split('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"')[1].split('","')[0]
			return feedback_id
		except:
			return False 
	def get_post2(self,id):
		cookie=self.cookie
		headers={'Host':'www.facebook.com','cache-control':'max-age=0','viewport-width':'980','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Linux"','sec-ch-prefers-color-scheme':'dark','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site':'same-origin','sec-fetch-mode':'navigate','sec-fetch-user':'?1','sec-fetch-dest':'document','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':cookie}
		try:
			self.url=requests.get('https://www.facebook.com/'+id,headers=headers).url
			home=requests.get(self.url,headers=headers).text
			feedback_id=home.split('private_reply_context":null,"feedback":{"id":"')[1].split('"')[0]
			return feedback_id
		except:
			return False 
	def like(self,id,type)->bool:
		feedback_id=self.get_post(id)
		if feedback_id==False:return False
		cookie=self.cookie
		ck_pro5=cookie+'; i_user='+self.id_page+';'
		list={'LIKE':'1635855486666999','LOVE':'1678524932434102','HAHA':'115940658764963','CARE':'613557422527858','WOW':'478547315650144','SAD':'908563459236466','ANGRY':'444813342392137'}
		cx=list[type]
		headers={'Host':'www.facebook.com','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','viewport-width':'980','content-type':'application/x-www-form-urlencoded','x-fb-lsd':'9Xdzx3CKd5TIvVw6C2JVum','x-fb-friendly-name':'CometUFIFeedbackReactMutation','sec-ch-prefers-color-scheme':'dark','sec-ch-ua-platform':'"Linux"','accept':'*/*','origin':'https://www.facebook.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':self.url,'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':ck_pro5}
		data={'av':self.id_page,'__user':self.id_page,'__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUFIFeedbackReactMutation','variables':'{"input":{"attribution_id_v2":"CometVideoHomeNewPermalinkRoot.react,comet.watch.injection,via_cold_start,1682819296134,664122,2392950137,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+cx+'","feedback_source":"VIDEO_HOME_FEED","is_tracking_encrypted":true,"tracking":[],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.id_page+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":2}','server_timestamps':'true','doc_id':'5703418209680126','fb_api_analytics_tags':'["qpl_active_flow_ids=30605361"]'}if '/videos/' in self.url else{'av':self.id_page,'__user':self.id_page,'__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUFIFeedbackReactMutation','variables':'{"input":{"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1672402199998,170308,,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+cx+'","feedback_source":"OBJECT","is_tracking_encrypted":true,"tracking":[""],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.id_page+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":2}','server_timestamps':'true','doc_id':'5703418209680126','fb_api_analytics_tags':'["qpl_active_flow_ids=30605361"]'}
		try:
			reac=requests.post('https://www.facebook.com/api/graphql/',headers=headers,data=data)
			return reac.json()['data']['feedback_react']['feedback']['viewer_actor']['id']==self.id_page
		except:
			return False
	def follow(self,id)->bool:
		ck_pro5=self.cookie+'; i_user='+self.id_page+';'
		headers={'Host':'www.facebook.com','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','viewport-width':'980','content-type':'application/x-www-form-urlencoded','x-fb-lsd':'ozBHo3fICOG_bXpKqo1J1C','x-fb-friendly-name':'CometUserFollowMutation','sec-ch-prefers-color-scheme':'light','sec-ch-ua-platform':'"Linux"','accept':'*/*','origin':'https://www.facebook.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.facebook.com/','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':ck_pro5}
		data={'av':self.id_page,'fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUserFollowMutation','variables':'{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1669330367418,219724,250100865708545,","subscribe_location":"PROFILE","subscribee_id":"'+id+'","actor_id":"'+self.id_page+'","client_mutation_id":"1"},"scale":2}','server_timestamps':'true','doc_id':'5032256523527306'}
		try:
			fl=requests.post('https://www.facebook.com/api/graphql/',headers=headers,data=data)
			return fl.json()['data']['actor_subscribe']['subscribee']['subscribe_status']=='IS_SUBSCRIBED'
		except:
			return False 
	def group(self,id)->bool:
		ck_pro5=self.cookie+'; i_user='+self.id_page+';'
		headers={'authority':'www.facebook.com','accept':'*/*','accept-language':'en-US,en;q=0.9,vi;q=0.8','content-type':'application/x-www-form-urlencoded','cookie':ck_pro5,'origin':'https://www.facebook.com','referer':'https://www.facebook.com/groups/'+id+'/?ref=share_group_link','sec-ch-prefers-color-scheme':'light','sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','viewport-width':'824','x-fb-friendly-name':'GroupCometJoinForumMutation','x-fb-lsd':'gUTCqdEnK_GG757IZ8OiXr',}
		data={'av':self.id_page,'fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupCometJoinForumMutation','variables':'{"feedType":"DISCUSSION","groupID":"'+id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1669693169873,34680,2361831622,","group_id":"'+id+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+self.id_page+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":false}','server_timestamps':'true','doc_id':'5608919199222447','fb_api_analytics_tags':'["qpl_active_flow_ids=431626709"]'}
		try:
			response=requests.post('https://www.facebook.com/api/graphql/',headers=headers,data=data)
			return id in response.text
		except:
			return False
	def page(self,id)->bool:
		ck_pro5=self.cookie+'; i_user='+self.id_page+';'
		headers={'Host':'www.facebook.com','sec-ch-ua':'"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','viewport-width':'980','x-fb-friendly-name':'CometPageLikeCommitMutation','x-fb-lsd':'jpvqXdpYwXQubs9Dlo1dZJ','content-type':'application/x-www-form-urlencoded','x-asbd-id':'198387','sec-ch-prefers-color-scheme':'dark','sec-ch-ua-platform':'"Linux"','accept':'*/*','origin':'https://www.facebook.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.facebook.com/'+id,'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':ck_pro5}
		data={'av':self.id_page,'__user':self.id_page,'fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometProfilePlusLikeMutation','variables':'{"input":{"attribution_id_v2":"CometSinglePageHomeRoot.react,comet.page,via_cold_start,1682575589156,174147,250100865708545,","is_tracking_encrypted":true,"page_id":'+id+',"source":"unknown","tracking":[],"actor_id":"'+self.id_page+'","client_mutation_id":"1"},"isAdminView":false}','server_timestamps':'true','doc_id':'5931408060305387',}
		try:
			response=requests.post('https://www.facebook.com/api/graphql/',headers=headers,data=data)
			return id in response.text
		except:
			return False
	def Nhap_Cookie(self):
		list_cookie=[]
		i=0
		while True:
			i+=1
			self.cookie=input(thanh_xau+f'Nhập Cookie Facebook Thứ {i}: '+vang)
			if self.cookie=='' and i>1:
				break
			name=self.get_thongtin()
			if name !=False:
				ten=name[0]
				print(f'{lam}Tên Facebook: {tim}{ten}')
				list_cookie.append(self.cookie)
				bongoc(14)
			else:
				print(f'{red}Cookie Facebook Die ! Vui Lòng Nhập Lại !!!')
				bongoc(14)
				i-=1
		return list_cookie
	def regpro5(self):
		banner()
		dem=0
		while True:
			if os.path.exists('Cookie_FB_Regpage_N-Tool.txt'):
				print(thanh_xau+f'Nhập {red}[{vang}1{red}]{luc} Sử Dụng Cookie Facebook Đã Lưu ')
				print(thanh_xau+f'Nhập {red}[{vang}2{red}]{luc} Nhập Cookie Facebook Mới')
				chon=input(thanh_xau+f'{luc}Vui Lòng Nhập: {vang}')
				if chon=='1':
					print(lam+' Đang Lấy Dữ Liệu Đã Lưu');sleep(1)
					with open('Cookie_FB_Regpage_N-Tool.txt','r')as f:
						list_cookie=json.loads(f.read())
						break
				elif chon=='2':
					os.remove('Cookie_FB_Regpage_N-Tool.txt'); bongoc(14)
				else:
					print(red+'Lựa Chọn Không Xác Định.'); bongoc(14); continue
			if not os.path.exists('Cookie_FB_Regpage_N-Tool.txt'):
				list_cookie=self.Nhap_Cookie()
				with open('Cookie_FB_Regpage_N-Tool.txt','w')as f:
					json.dump(list_cookie,f)
				break
		banner()
		print(thanh_xau+f'Số Cookie: {vang}{len(list_cookie)} ')
		bongoc(14)
		delay=int(input(thanh_xau+f'Nhập Delay (Trên 1000): {vang}'))
		avt=input(thanh_xau+'Bạn Có Muốn Auto Up Avatar (y/n): '+vang)
		if avt=='y' or avt=='Y':
			bia=input(thanh_xau+'Bạn Có Muốn Auto Up Ảnh Bìa (y/n): '+vang)
		else:
			bia=''
		doinick=int(input(thanh_xau+f'Sau Bao Nhiêu Page Thì Đổi Nick:{vang} '))
		bongoc(14)
		while True:
			if len(list_cookie)==0:
				print(red+'Đã Xoá Tất Cả Cookie, Vui Lòng Nhập Lại  ')
				list_cookie=self.Nhap_Cookie()
				with open('Cookie_FB_Regpage_N-Tool.txt','w')as f:
					json.dump(list_cookie,f)
			for self.cookie in list_cookie:
				name=self.get_thongtin()
				if name !=False:
					ten=name[0]
					id=name[1]
				else:
					id=self.cookie.split('c_user=')[1].split(';')[0]
					print(f'{red}Cookie Tài Khoản {vang}{id} {red}Die',end='\r');sleep(3); print('                                     ',end='\r')
					list_cookie.remove(self.cookie)
					continue
				print(f'{luc}Đang Chạy ID FB:{vang} {id}{red} | {luc}Tên FB: {vang}{ten}')
				while True:
					reg=self.regpage()
					if reg:
						dem+=1
						print(f'{vang}[{trang}{dem}{vang}] {red}| {lam}{datetime.now().strftime("%H:%M:%S")} {red}|{vang} REG_PAGE {red}| {trang}{self.id_page} {red}| {lam}{self.name_page}')
						if avt=='y' or avt=='Y':
							up=self.upavt()
							if up:
								print(f'{vang}[{trang}{dem}{vang}] {red}| {lam}{datetime.now().strftime("%H:%M:%S")} {red}|{vang} UP_AVATAR {red}| {trang}{self.id_page} {red}| {lam}{self.name_page} ')
								if bia=='y' or bia=='Y':
									upp=self.upbia()
									print(f'{vang}[{trang}{dem}{vang}] {red}| {lam}{datetime.now().strftime("%H:%M:%S")} {red}|{vang} UP_ẢNH_BÌA {red}| {trang}{self.id_page} {red}| {lam}{self.name_page} ')
							else:
								print(f'{vang}[{trang}{dem}{vang}] {red}| {lam}{datetime.now().strftime("%H:%M:%S")} {red}|{vang} UP_AVATAR {red}| {trang}{self.id_page} {red}| {lam}{self.name_page}{red} | ERROR ')
						nghingoi(delay)
						if dem % doinick==0:break
					else:
						name=self.get_thongtin()
						if name==False:
							print(f' {red} Cookie Tài Khoản{vang} {ten} {red}Đã Bị Out !!!  ')
						else:
							print(f' {red}Tài Khoản{vang} {ten} {red}Đã Bị Block !!!	')
						list_cookie.remove(self.cookie)
						break
	def run(self):
		ntool=0
		dem=0
		banner()
		while True:
			if os.path.exists('configtds.txt'):
				with open('configtds.txt','r')as f:
					token=f.read()
				tds=TraoDoiSub_Api(token)
				data=tds.main()
				try:
					print(thanh_xau+f'Nhập {vang}[{trang}1{vang}] {luc}Giữ Lại Tài Khoản {vang}'+data['user'])
					print(thanh_xau+f'Nhập {vang}[{trang}2{vang}] {luc}Nhập Access_Token TDS Mới')
					chon=input(thanh_xau+f'{luc}Nhập {trang}===>: {vang}')
					if chon=='2':
						os.remove('configtds.txt')
					elif chon=='1':
						pass
					else:
						print(f'{red}Lựa chọn không xác định !!!');bongoc(14)
						continue 
				except:
					os.remove('configtds.txt')
			if not os.path.exists('configtds.txt'):
				token=input(thanh_xau+f'Nhập Access_Token TDS: ')
				with open('configtds.txt','w')as f:
					f.write(token)
			with open('configtds.txt','r')as f:
				token=f.read()
			tds=TraoDoiSub_Api(token)
			data=tds.main()
			try:
				xu=data['xu']
				xudie=data['xudie']
				user=data['user']
				print(lam+' Đăng Nhập Thành Công ')
				break
			except:
				print(red+'Access Token Không Hợp Lệ! Xin Thử Lại ')
				os.remove('configtds.txt')
				continue 
		bongoc(14)
		while True:
			if os.path.exists('Cookie_Facebook_Profile_N-Tool.txt'):
				print(thanh_xau+f'Nhập {red}[{vang}1{red}]{luc} Sử Dụng Cookie Facebook Đã Lưu ')
				print(thanh_xau+f'Nhập {red}[{vang}2{red}]{luc} Nhập Cookie Facebook Mới')
				chon=input(thanh_xau+f'{luc}Vui Lòng Nhập: {vang}')
				if chon=='1':
					print(lam+' Đang Lấy Dữ Liệu Đã Lưu')#;sleep(1)
					with open('Cookie_Facebook_Profile_N-Tool.txt','r')as f:
						self.cookie=f.read()
				elif chon=='2':
					os.remove('Cookie_Facebook_Profile_N-Tool.txt'); bongoc(14)
				else:
					print(red+'Lựa Chọn Không Xác Định.'); bongoc(14); continue
			if not os.path.exists('Cookie_Facebook_Profile_N-Tool.txt'):
				while True:
					self.cookie=input(thanh_xau+luc+'Nhập Cookie Facebook: '+vang)
					name=self.get_thongtin()
					if name !=False:
						print(f'{tim}Tên Facebook: {lam}{name[0]}')
						with open('Cookie_Facebook_Profile_N-Tool.txt','w')as f:
							f.write(self.cookie)
					else:
						print(f'{red}Cookie Facebook Die ! Vui Lòng Nhập Lại !!!')
						bongoc(14)
						continue
					break
			name=self.get_thongtin()
			if name==False:print(f'{red}Cookie Facebook Die ! Vui Lòng Nhập Lại !!!'); os.remove('Cookie_Facebook_Profile_N-Tool.txt'); bongoc(14);continue
			get_page=self.get_pro5()
			if get_page==False or get_page[0]==0:
				print(red+'Không Tìm Thấy Page Profile ')
				continue 
			break
		page=[]
		list_page=[]
		banner()
		print(thanh_xau+luc+f'Tìm Thấy {get_page[0]} Page Profile')
		for i in range(len(get_page[1])):
			print(thanh_xau+f"Nhập {red}[{vang}{i+1}{red}]{luc} Để Chạy Page: {vang}{get_page[1][i]['profile']['name']}{red} | {luc}ID: {vang}{get_page[1][i]['profile']['id']} ")
			page.append([get_page[1][i]['profile']['name'],get_page[1][i]['profile']['id']])
		print(thanh_xau+f"Nhập {red}[{vang}all{red}]{luc} Để Chạy Tất Cả Page ")
		print(thanh_xau+f'{lam}Có Thể Chọn Nhiều Page (Cách Nhau Bởi Dấu +, Ví Dụ 1+2+3+...)')
		while True:
			chon=input(thanh_xau+f'{luc}Nhập {trang}===>: {vang}').split('+')
			if chon[0]=='all':
				list_page=page
				break
			try:
				for i in list(map(int,chon)):
					list_page.append(page[i-1])
				break
			except:
				list_page=[]
				print(red+'Lựa Chọn Không Xác Định Hãy Thử Lại ')
		banner()
		print(thanh_xau+f'Tên Tài Khoản: {vang}{user} ')
		print(thanh_xau+f'Xu Hiện Tại: {vang}{xu}')
		print(thanh_xau+f'Xu Bị Phạt: {vang}{xudie} ')
		print(thanh_xau+f'Số Page Đang Chạy: {vang}{len(list_page)} ')
		bongoc(14)
		print(thanh_xau+f' Nhập {vang}[{trang}1{vang}] {luc}Để Chạy Nhiệm Vụ Like')
		print(thanh_xau+f' Nhập {vang}[{trang}2{vang}] {luc}Để Chạy Nhiệm Vụ Like 2')
		print(thanh_xau+f' Nhập {vang}[{trang}3{vang}] {luc}Để Chạy Nhiệm Vụ Comment {vang}Đang Update')
		print(thanh_xau+f' Nhập {vang}[{trang}4{vang}] {luc}Để Chạy Nhiệm Vụ Share {vang}Đang Update')
		print(thanh_xau+f' Nhập {vang}[{trang}5{vang}] {luc}Để Chạy Nhiệm Vụ Cảm Xúc')
		print(thanh_xau+f' Nhập {vang}[{trang}6{vang}] {luc}Để Chạy Nhiệm Vụ Follow')
		print(thanh_xau+f' Nhập {vang}[{trang}7{vang}] {luc}Để Chạy Nhiệm Vụ Like Page')
		print(thanh_xau+f' Nhập {vang}[{trang}8{vang}] {luc}Để Chạy Nhiệm Vụ Cảm Xúc CMT {vang}Đang Update')
		print(thanh_xau+f' Nhập {vang}[{trang}9{vang}] {luc}Để Chạy Nhiệm Vụ Group')
		print(thanh_xau+f'{lam}Có Thể Chọn Nhiều Nhiệm Vụ (Ví Dụ 123...)')
		bongoc(14)
		nhiemvu=input(thanh_xau+f'Nhập Số Để Chạy Nhiệm Vụ:{vang} ')
		list_nv=[]
		if '1' in nhiemvu:list_nv.append('like')
		if '2' in nhiemvu:list_nv.append('likegiare')
		if '3' in nhiemvu:list_nv.append('comment')
		if '4' in nhiemvu:list_nv.append('share')
		if '5' in nhiemvu:list_nv.append('reaction')
		if '6' in nhiemvu:list_nv.append('follow')
		if '7' in nhiemvu:list_nv.append('page')
		if '8' in nhiemvu:list_nv.append('reactcmt')
		if '9' in nhiemvu:list_nv.append('group')
		delaymin=''
		#int(input(thanh_xau+f'Nhập Delay Min: {vang}'))
		delaymax=''
		#int(input(thanh_xau+f'Nhập Delay Max:{vang} '))
	#	print(thanh_xau+f'Sau ____ Nhiệm Vụ Thì Kích Hoạt Chống Block.',end='\r')
		nvblock='99999'
		#int(input(thanh_xau+f'Sau{vang} '))
	#	print(thanh_xau+f'Sau {vang}{nvblock} {luc}Nhiệm Vụ Nghỉ Ngơi ____ Giây       ',end='\r')
		delaybl='0'
		#int(input(thanh_xau+f'Sau {vang}{nvblock} {luc}Nhiệm Vụ Nghỉ Ngơi {vang}'))
		doinick='99999'
		#int(input(thanh_xau+f'Sau Bao Nhiêu Nhiệm Vụ Thì Đổi Nick:{vang} '))
		bongoc(14)
		while True:
			ntool=0
			if len(list_page)==0:
				print(red+'Đã Xoá Tất Cả Page, Vui Lòng Nhập Lại  ')
				while True:
					self.cookie=input(thanh_xau+luc+'Nhập Cookie Facebook: '+vang)
					name=self.get_thongtin()
					if name !=False:
						print(f'{tim}Tên Facebook: {lam}{name[0]}')
						with open('Cookie_Facebook_Profile_N-Tool.txt','w')as f:
							f.write(self.cookie)
					else:
						print(f'{red}Cookie Facebook Die ! Vui Lòng Nhập Lại !!!')
						bongoc(14)
						continue
					get_page=self.get_pro5()
					if get_page==False or get_page[0]==0:
						print(red+'Không Tìm Thấy Page Profile ')
						bongoc(14)
						continue 
					print(thanh_xau+luc+f'Tìm Thấy {get_page[0]} Page Profile')
					break
				page=[]
				list_page=[]
				bongoc(14)
				for i in range(len(get_page[1])):
					print(thanh_xau+f"Nhập {red}[{vang}{i+1}{red}]{luc} Để Chạy Page Name: {vang}{get_page[1][i]['profile']['name']}{red} | {luc}ID: {vang}{get_page[1][i]['profile']['id']} ")
					page.append([get_page[1][i]['profile']['name'],get_page[1][i]['profile']['id']])
				print(thanh_xau+f'{lam}Có Thể Chọn Nhiều Page (Cách Nhau Bởi Dấu +, Ví Dụ 1+2+3+...)')
				while True:
					try:
						for i in list(map(int,input(thanh_xau+f'{luc}Nhập {trang}===>: {vang}').split('+'))):
							list_page.append(page[i-1])
						break
					except:
						list_page=[]
						print(red+'Lựa Chọn Không Xác Định Hãy Thử Lại ')
					bongoc(14)
			for page in list_page:
				if ntool==2:break
				list_loi={'likegiare':0,'like':0,'comment':0,'share':0,'reaction':0,'follow':0,'page':0,'group':0,'reactcmt':0}
				ntool=0
				loi=0
				cau_hinh=tds.run(page[1])
				self.id_page=page[1]
				if cau_hinh==True:
					print(f'{luc}Đang Cấu Hình ID Page:{vang} {page[1]}{red} | {luc}Tên Page: {vang}{page[0]}')
				else:
					print(f'{red}Cấu Hình Thất Bại ID Page: {page[1]} | Tên Page: {page[0]} ',end='\r')
					continue
				while True:
					if ntool==1 or ntool==2:break 
					for nv in list_nv:
						if ntool==1 or ntool==2:break 
						listnv=tds.get_job(nv)
						if listnv==False:
							print(f'Không Get Được Nhiệm Vụ {nv.upper()} ',end='\r');sleep(1); print('                                                        ',end='\r')
						elif '"error":' in listnv.text:
							if listnv.json()['error']=='Thao tác quá nhanh vui lòng chậm lại':
								coun=listnv.json()['countdown']
								#print(f'{red}Đang Get Nhiệm Vụ {nv.upper()}, COUNTDOWN: {str(round(coun, 3))}              ',end='\r'); sleep(2); print('                                                       ',end='\r')
							else:
								print(red+listnv.json()['error'],end='\r')
						else:
							listnv=listnv.json()
							if len(listnv)==0:
							#	print(red+f'Hết Nhiệm Vụ {nv.upper()}                    ',end='\r');sleep(1); print('                                                        ',end='\r')
								nvlike=0
							else:
							#	print(f'{luc}Tìm Thấy {vang}{len(listnv)} {luc}Nhiệm Vụ {nv.upper()}              ',end='\r')
								for x in listnv:
									if nv=='like':
										id=x['id']
										like=self.like(id,'LIKE')
										type=nv.upper()
									elif nv=='likegiare':
										id=x['id']
										like=self.like(id,'LIKE')
										type=nv.upper()
									elif nv=='comment':
										id=x['id']
										nd=x['msg']
										type=nv.upper()
									elif nv=='share':
										id=x['id']
										type=nv.upper()
										self.share(id)
									elif nv=='reaction':
										id=x['id']
										type=x['type']
										like=self.like(id,type)
									elif nv=='follow':
										id=x['id']
										follow=self.follow(id)
										type=nv.upper()
									elif nv=='page':
										id=x['id']
										like_page=self.page(id)
										type=nv.upper()
									elif nv=='reactcmt':
										id=x['id']
										type=x['type']
										type=type+'CMT'
									elif nv=='group':
										id=x['id']
										groups=self.group(id)
										type=nv.upper()
									nhan=tds.nhan_xu(type,id)
									try:
										xu=nhan[1]
										msg=nhan[0]
										dem+=1
										list_loi[nv]=0
										hoanthanh(dem,id,type,msg,xu)
										if dem % doinick==0:
											bongoc(14); print(f'{lam}Số Xu Hiện Tại: {vang}{xu} {red}| {lam}Số Page Đang Chạy: {vang}{len(list_page)}'); bongoc(14); ntool=1; break
										if dem % nvblock==0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin,delaymax)
									except:
										list_loi[nv]+=1
										error(id,type)
									if list_loi[nv]>=10:
										name2=self.get_thongtin()
										if name2==False:
											print(f' {red} Cookie Tài Khoản{vang} {name[0]} {red}Đã Bị Out !!!                ')
											bongoc(14)
											list_page=[];ntool=2;break
										else:
											print(f' {red}Page{vang} {page[0]} {red}Đã Bị Block {nv} !!!					')
											bongoc(14)
											list_page.remove(page);ntool=1;break
	def run_ttc(self):
		total=0
		dem=0
		ntool=0
		banner()
		while True:
			if os.path.exists('configttc.txt'):
				with open('configttc.txt','r')as f:
					token=f.read()
				ttc=TuongTacCheo_Api(token)
				data=ttc.login()
				if data !=False:
					print(thanh_xau+f'Nhập {vang}[{trang}1{vang}] {luc}Giữ Lại Tài Khoản {vang}'+data[0])
					print(thanh_xau+f'Nhập {vang}[{trang}2{vang}] {luc}Nhập Access_Token TTC Mới')
					chon=input(thanh_xau+f'{luc}Nhập {trang}===>: {vang}')
					if chon=='2':
						os.remove('configttc.txt')
					elif chon=='1':
						pass
					else:
						print(red+'Lựa chọn không xác định !!!');bongoc(14)
						continue 
				else:
					os.remove('configttc.txt')
			if not os.path.exists('configttc.txt'):
				token=input(thanh_xau+f'Nhập Access_Token TTC: ')
				with open('configttc.txt','w')as f:
					f.write(token)
			with open('configttc.txt','r')as f:
				token=f.read()
			ttc=TuongTacCheo_Api(token)
			data=ttc.login()
			if data !=False:
				xu=data[1]
				user=data[0]
				print(lam+' Đăng Nhập Thành Công ')
				break
			else:
				os.remove('configttc.txt')
				continue 
		bongoc(14)
		while True:
			if os.path.exists('Cookie_Facebook_Profile_TTC_N-Tool.txt'):
				print(thanh_xau+f'Nhập {red}[{vang}1{red}]{luc} Sử Dụng Cookie Facebook Đã Lưu ')
				print(thanh_xau+f'Nhập {red}[{vang}2{red}]{luc} Nhập Cookie Facebook Mới')
				chon=input(thanh_xau+f'{luc}Vui Lòng Nhập: {vang}')
				if chon=='1':
					print(lam+' Đang Lấy Dữ Liệu Đã Lưu')#;sleep(1)
					with open('Cookie_Facebook_Profile_TTC_N-Tool.txt','r')as f:
						self.cookie=f.read()
				elif chon=='2':
					os.remove('Cookie_Facebook_Profile_TTC_N-Tool.txt'); bongoc(14)
				else:
					print(red+'Lựa Chọn Không Xác Định.'); bongoc(14); continue
			if not os.path.exists('Cookie_Facebook_Profile_TTC_N-Tool.txt'):
				while True:
					self.cookie=input(thanh_xau+luc+'Nhập Cookie Facebook: '+vang)
					name=self.get_thongtin()
					if name !=False:
						print(f'{tim}Tên Facebook: {lam}{name[0]}')
						with open('Cookie_Facebook_Profile_TTC_N-Tool.txt','w')as f:
							f.write(self.cookie)
					else:
						print(f'{red}Cookie Facebook Die ! Vui Lòng Nhập Lại !!!')
						bongoc(14)
						continue
					break
			name=self.get_thongtin()
			if name==False:print(f'{red}Cookie Facebook Die ! Vui Lòng Nhập Lại !!!'); os.remove('Cookie_Facebook_Profile_TTC_N-Tool.txt'); bongoc(14);continue
			get_page=self.get_pro5()
			if get_page==False or get_page[0]==0:
				print(red+'Không Tìm Thấy Page Profile ')
				continue 
			break
		page=[]
		list_page=[]
		banner()
		print(thanh_xau+luc+f'Tìm Thấy {get_page[0]} Page Profile')
		for i in range(len(get_page[1])):
			print(thanh_xau+f"Nhập {red}[{vang}{i+1}{red}]{luc} Để Chạy Page: {vang}{get_page[1][i]['profile']['name']}{red} | {luc}ID: {vang}{get_page[1][i]['profile']['id']} ")
			page.append([get_page[1][i]['profile']['name'],get_page[1][i]['profile']['id']])
		print(thanh_xau+f"Nhập {red}[{vang}all{red}]{luc} Để Chạy Tất Cả Page ")
		print(thanh_xau+f'{lam}Có Thể Chọn Nhiều Page (Cách Nhau Bởi Dấu +, Ví Dụ 1+2+3+...)')
		while True:
			chon=input(thanh_xau+f'{luc}Nhập {trang}===>: {vang}').split('+')
			if chon[0]=='all':
				list_page=page
				break
			try:
				for i in list(map(int,chon)):
					list_page.append(page[i-1])
				break
			except:
				list_page=[]
				print(red+'Lựa Chọn Không Xác Định Hãy Thử Lại ')
		banner()
		print(thanh_xau+f'Tên Tài Khoản: {vang}{user} ')
		print(thanh_xau+f'Xu Hiện Tại: {vang}{xu}')
		print(thanh_xau+f'Số Page Đang Chạy: {vang}{len(list_page)} ')
		bongoc(14)
		print(thanh_xau+f' Nhập {vang}[{trang}1{vang}] {luc}Để Chạy Nhiệm Vụ Like')
		print(thanh_xau+f' Nhập {vang}[{trang}2{vang}] {luc}Để Chạy Nhiệm Vụ Comment {vang}Đang Update')
		print(thanh_xau+f' Nhập {vang}[{trang}3{vang}] {luc}Để Chạy Nhiệm Vụ Share {vang}Đang Update')
		print(thanh_xau+f' Nhập {vang}[{trang}4{vang}] {luc}Để Chạy Nhiệm Vụ Share Kèm Nội Dung {vang}Đang Update')
		print(thanh_xau+f' Nhập {vang}[{trang}5{vang}] {luc}Để Chạy Nhiệm Vụ Cảm Xúc')
		print(thanh_xau+f' Nhập {vang}[{trang}6{vang}] {luc}Để Chạy Nhiệm Vụ Follow')
		print(thanh_xau+f' Nhập {vang}[{trang}7{vang}] {luc}Để Chạy Nhiệm Vụ Like Page')
		print(thanh_xau+f' Nhập {vang}[{trang}8{vang}] {luc}Để Chạy Nhiệm Vụ Cảm Xúc CMT {vang}Đang Update')
		print(thanh_xau+f' Nhập {vang}[{trang}9{vang}] {luc}Để Chạy Nhiệm Vụ Group')
		print(thanh_xau+f'{lam}Có Thể Chọn Nhiều Nhiệm Vụ (Ví Dụ 123...)')
		bongoc(14)
		nhiemvu=input(thanh_xau+f'Nhập Số Để Chạy Nhiệm Vụ:{vang} ')
		list_nv=[]
		if '1' in nhiemvu:list_nv.append('')
		if '2' in nhiemvu:list_nv.append('/cmtcheo')
		if '3' in nhiemvu:list_nv.append('/sharecheo')
		if '4' in nhiemvu:list_nv.append('/sharecheokemnoidung')
		if '5' in nhiemvu:list_nv.append('/camxuccheo')
		if '6' in nhiemvu:list_nv.append('/subcheo')
		if '7' in nhiemvu:list_nv.append('/likepagecheo')
		if '8' in nhiemvu:list_nv.append('/camxuccheobinhluan')
		if '9' in nhiemvu:list_nv.append('/thamgianhomcheo')
		list_loai={'':'LIKE','/cmtcheo':'COMMENT','/sharecheokemnoidung':'SHARE','/sharecheo':'SHARE','/camxuccheo':'REACTION','/subcheo':'FOLLOW','/likepagecheo':'PAGE','/camxuccheobinhluan':'REACTION CMT','/thamgianhomcheo':'GROUP'}
		delaymin=int(input(thanh_xau+f'Nhập Delay Min: {vang}'))
		delaymax=int(input(thanh_xau+f'Nhập Delay Max:{vang} '))
		print(thanh_xau+f'Sau ____ Nhiệm Vụ Thì Kích Hoạt Chống Block.',end='\r')
		nvblock=int(input(thanh_xau+f'Sau{vang} '))
		print(thanh_xau+f'Sau {vang}{nvblock} {luc}Nhiệm Vụ Nghỉ Ngơi ____ Giây       ',end='\r')
		delaybl=int(input(thanh_xau+f'Sau {vang}{nvblock} {luc}Nhiệm Vụ Nghỉ Ngơi {vang}'))
		doinick=int(input(thanh_xau+f'Sau Bao Nhiêu Nhiệm Vụ Thì Đổi Nick:{vang} '))
		bongoc(14)
		while True:
			ntool=0
			if len(list_page)==0:
				print(red+'Đã Xoá Tất Cả Page, Vui Lòng Nhập Lại  ')
				while True:
					self.cookie=input(thanh_xau+luc+'Nhập Cookie Facebook: '+vang)
					name=self.get_thongtin()
					if name !=False:
						print(f'{tim}Tên Facebook: {lam}{name[0]}')
						with open('Cookie_Facebook_Profile_N-Tool.txt','w')as f:
							f.write(self.cookie)
					else:
						print(f'{red}Cookie Facebook Die ! Vui Lòng Nhập Lại !!!')
						bongoc(14)
						continue
					get_page=self.get_pro5()
					if get_page==False or get_page[0]==0:
						print(red+'Không Tìm Thấy Page Profile ')
						bongoc(14)
						continue 
					print(thanh_xau+luc+f'Tìm Thấy {get_page[0]} Page Profile')
					break
				page=[]
				list_page=[]
				bongoc(14)
				for i in range(len(get_page[1])):
					print(thanh_xau+f"Nhập {red}[{vang}{i+1}{red}]{luc} Để Chạy Page Name: {vang}{get_page[1][i]['profile']['name']}{red} | {luc}ID: {vang}{get_page[1][i]['profile']['id']} ")
					page.append([get_page[1][i]['profile']['name'],get_page[1][i]['profile']['id']])
				print(thanh_xau+f'{lam}Có Thể Chọn Nhiều Page (Cách Nhau Bởi Dấu +, Ví Dụ 1+2+3+...)')
				while True:
					try:
						for i in list(map(int,input(thanh_xau+f'{luc}Nhập {trang}===>: {vang}').split('+'))):
							list_page.append(page[i-1])
						break
					except:
						list_page=[]
						print(red+'Lựa Chọn Không Xác Định Hãy Thử Lại ')
					bongoc(14)
			for page in list_page:
				list_loi={'':0,'/cmtcheo':0,'/sharecheo':0,'/sharecheokemnoidung':0,'/camxuccheo':0,'/subcheo':0,'/likepagecheo':0,'/thamgianhomcheo':0,'/camxuccheobinhluan':0}
				if ntool==2:break
				ntool=0
				loi=0
				cau_hinh=ttc.run(page[1])
				self.id_page=page[1]
				if cau_hinh==True:
					print(f'{luc}Đang Cấu Hình ID Page:{vang} {page[1]}{red} | {luc}Tên Page: {vang}{page[0]}')
				else:
					print(f'{red}Cấu Hình Thất Bại ID Page: {page[1]} | Tên Page: {page[0]} ',end='\r')
					continue
				while True:
					if ntool==1 or ntool==2:break 
					for nv in list_nv:
						print(1)
						if ntool==1 or ntool==2:break 
						list_nv=ttc.getnv(nv)
						if list_nv==False:
							print(red+f'Không Get Được Nhiệm Vụ {list_loai[nv]}',end='\r'); continue
						elif len(list_nv)==0:
							print(red+f'Hết Nhiệm Vụ {list_loai[nv]}                    ',end='\r');sleep(1); print('                                                        ',end='\r'); continue 
						else:
							print(f'{luc}Tìm Thấy {vang}{len(list_nv)} {luc}Nhiệm Vụ {list_loai[nv]}',end='\r')
							for x in list_nv:
								if nv=='':
									id=x['idpost']
									type='LIKE'
									like=self.like(id,'LIKE')
								elif nv=='/cmtcheo':
									type=1
									id=x['idpost']
								elif nv=='/sharecheo':
									id=x['idpost']
									type=1
								elif nv=='/camxuccheo':
									id=x['idpost']
									type=x['loaicx']
									like=self.like(id,type)
								elif nv=='/subcheo':
									id=x['idpost']
									follow=self.follow(id)
									type=1
								elif nv=='/likepagecheo':
									id=x['idpost']
									like_page=self.page(id)
									type=1
								elif nv=='reactcmt':
									id=x['idpost']
								elif nv=='/thamgianhomcheo':
									id=x['idpost']
									type=1
									groups=self.group(id)
								nhan=ttc.nhanxu2(id,nv,type)
								xus=ttc.coin()
								if 'Thành công' in nhan and xus !=xu and xus !=False:
									dem+=1; xu=xus; total=total+(int(xus)-int(xu))
									hoanthanh(dem,id,type,str(int(xus)-int(xu)))
									if dem % 10==0:show(user,xu,total)
									if dem % doinick==0:ntool=1; break
									if dem % nvblock==0:chongblock(delaybl)
									else:nghingoi(delaymin,delaymax)
								else:list_loi[nv]+=1;error(id,type)
								if list_loi[nv]>=10:
									name2=self.get_thongtin()
									if name2==False:
										print(f' {red} Cookie Tài Khoản{vang} {name[0]} {red}Đã Bị Out !!!                ')
										bongoc(14)
										list_page=[];ntool=2;break
									else:
										print(f' {red}Page{vang} {page[0]} {red}Đã Bị Block {list_loai[nv]} !!!					')
										bongoc(14)
										list_page.remove(page);ntool=1;break
class Facebook_Api(object):
	def __init__(self,cookie):
		self.cookie=cookie
		self.headers={'authority':'mbasic.facebook.com','cache-control':'max-age=0','sec-ch-ua':'"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','upgrade-insecure-requests':'1','origin':'https://mbasic.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site':'same-origin','sec-fetch-mode':'navigate','sec-fetch-user':'?1','sec-fetch-dest':'document','referer':'https://mbasic.facebook.com/','accept-language':'en-US,en;q=0.9','cookie':cookie}
	def get_thongtin(self):
		try:
			home=requests.get('https://mbasic.facebook.com/profile.php',headers=self.headers).text
			self.fb_dtsg=home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
			self.jazoest=home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
			ten=home.split('<title>')[1].split('</title>')[0]
			self.user_id=self.cookie.split('c_user=')[1].split(';')[0]
			return ten,self.user_id
		except:
			return 0
	def follow(self,id):
		data={'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHxqUW13xt0mUyEqxenFwLBwopU98nwgU765QdwSxucyU8EW1twYwJyEiwsobo6u3y4o11U2nwb-q7oc81xoswIK1Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61uwZwlo5qfK0zEkxe2GewyDwsoqBwJK2W5olwUwgojUlDw-wSU72m7-8wywdG7FobpEbUGdwb6223908O3216AzUjwTwNxe6Uak1xwJwxw','__csr':'hcp2vsTfcyBblX4JmmZOiFYKx7KWi_qT9jkxbOfKAAlXWmHGGlq8kNsOVanp9WDQKEHXKRWGulGhaAHHy8VeiWGuUGVoyQUFaui54cCHpp-WCxqHyV9qyUx153qzoWE8ql3pEG4p8pyVGCyooCxe5ojBy98aHG4Eb8mG269Vby8be4oGUO9whXxa2q2q49okyoy26q1BwYxe4E6W10y88E467Erzo6-2y5Etxl3UO2GWwaeu3-7o7uaw922t08K026O03iuC04f802PRw4bw2v80za0G80B-0b-e09dBw0Uww2DOw0jP80n7g3Iw1k208bzE1lU8E','__req':'5','__hs':'9362.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'GOOD','__rev':'1006788684','__s':'p2x8mf:qj6dvy:bj8e46','__hsi':'7185171904183015509','__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'lsd':'afdisHHGuglOo_hNSDt3Fb','__aaid':'775223720487728','__spin_r':'1006788684','__spin_b':'trunk','__spin_t':'1672928199','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUserFollowMutation','variables':'{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1672928202199,140922,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+id+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":2}','server_timestamps':'true','doc_id':'5032256523527306',}
		headers={'Host':'www.facebook.com','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','viewport-width':'980','content-type':'application/x-www-form-urlencoded','x-fb-lsd':'afdisHHGuglOo_hNSDt3Fb','x-fb-friendly-name':'CometUserFollowMutation','sec-ch-prefers-color-scheme':'dark','sec-ch-ua-platform':'"Linux"','accept':'*/*','origin':'https://www.facebook.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.facebook.com/'+id,'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':self.cookie}
		try:
			fl=requests.post('https://www.facebook.com/api/graphql/',headers=headers,data=data)
			if 'IS_SUBSCRIBED' in fl.text:
				return True
			else:
				return fl
		except:
			return False 
	def page(self,id):
		data={'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwAyU8EW0CEboG4E762S1DwUx60gu0BU2_CxS320om78bbwto88422y11xmfz83WwgEcHzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK0zEkxe2GewGwkUtxGm2SUbElxm3y11xfxmu3W2i4U72m7-8wywfCm2Sq2-azo2NwwwOg2cwMwhF8-4UdUcojxK2B0oobo8o','__csr':'g8JNc9n2tWr5W4til-I_On8J9rshlR8nZFiELH_Hnij4JfOJLOGiLoxLBlGRuZaGF4CZddQ4L_JfCiDKWVryuiqqFAcy8x6CBtqJkF8ZVExauAbgOtLAG5FUGFptxqfxi4Hzaz8CQ2SaxC9xCi48Wqqq11g8EaoS9g9U4m224oG68sGucx68wyg6G22mfxa4Xxq7EKbwi82LwNxu48c814EC2K3O5U-2WEhCxO1EwioeUiwiE6e3HwTw18C02k-0exw0deO0jV05Swe20bTw5_w1zF03I202po6e07Co0K6Zlw0jjo0E-0qW08ug8UhBw21e0fLw5Ww9K0Z86u','__req':'o','__hs':'19363.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'GOOD','__rev':'1006793331','__s':'v80lqo:poayhk:qxdcmk','__hsi':'7185553908092803679','__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'lsd':'V64c7kKr5hAtzX2IIDgKp8','__aaid':'775223720487728','__spin_r':'1006793331','__spin_b':'trunk','__spin_t':'1673017141','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometPageLikeCommitMutation','variables':'{"input":{"attribution_id_v2":"CometSinglePageHomeRoot.react,comet.page,via_cold_start,1673017144344,576155,250100865708545,","is_tracking_encrypted":true,"page_id":"'+id+'","source":"unknown","tracking":[],"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"isAdminView":false}','server_timestamps':'true','doc_id':'5491200487600992',}
		headers={'Host':'www.facebook.com','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','viewport-width':'980','content-type':'application/x-www-form-urlencoded','x-fb-lsd':'V64c7kKr5hAtzX2IIDgKp8','x-fb-friendly-name':'CometPageLikeCommitMutation','sec-ch-prefers-color-scheme':'dark','sec-ch-ua-platform':'"Linux"','accept':'*/*','origin':'https://www.facebook.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.facebook.com/'+id,'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':self.cookie}
		try:
			page=requests.post('https://www.facebook.com/api/graphql/',headers=headers,data=data)
			if 'FOLLOW' in page.text:
				return True
			else:
				return page.text
		except:
			return False
	def group(self,id):
			headers={'Host':'www.facebook.com','sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','viewport-width':'980','content-type':'application/x-www-form-urlencoded','x-fb-lsd':'gKT7R4dxIBjI4wUDUP5ivT','x-fb-friendly-name':'GroupCometJoinForumMutation','sec-ch-prefers-color-scheme':'dark','sec-ch-ua-platform':'"Linux"','accept':'*/*','origin':'https://www.facebook.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.facebook.com/groups/'+id+'/','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':self.cookie}
			data={'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHJ16U9ob8ng5K8G6EjBWo2nDwAxu13wsongS3q2ibwyzE2qwJyEiwsobo6u3y4o2Gwfi0LVEtwMw65xO321Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-U2exi4UaEW2G1jxS6FobrwKxm5oe8464-5pUfEe88o4Wm7-8xmcwfCm2CVEbUGdG1Fwh888cA0z8c84qifxe3u364UrwFg662S26','__csr':'gadNAIYllhsKOE8IpidFPhcIx34Omy9-O9OO8hZ_8-kAymHGAybJqGlvmWl7nWBWJ7GqaXHz7GFe9oy_KBl7h6h4KVah94QeKVHACDyryqKdF5GuXXBCgNpbJ5jjGm8yQEWrCixl6xWuiih5yo-8wAy84mq4poN0Vzbxe16whAufgO5U8UKi4Eyu4EjwGK78527o8411wgocU5u1MwSwFyU8Uf8igaElw8e9xK2GewNgy5o5m1nDwLwrokm16www8G03cy0arw0Zyw0aaC0mG0eJzl8ow2Jw6tw44w4uzo045W1UgSeg0z-07X81-E0cNo0By1Wwi8fE0lYw2h81a8gw9u','__req':'k','__hs':'19363.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'EXCELLENT','__rev':'1006794317','__s':'gtlvj8:fxbzro:f2kk19','__hsi':'7185658639628512803','__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'lsd':'gKT7R4dxIBjI4wUDUP5ivT','__aaid':'1576489885859472','__spin_r':'1006794317','__spin_b':'trunk','__spin_t':'1673041526','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupCometJoinForumMutation','variables':'{"feedType":"DISCUSSION","groupID":"'+id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1673041528761,114928,2361831622,","group_id":"'+id+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":2,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":false}','server_timestamps':'true','doc_id':'5853134681430324','fb_api_analytics_tags':'["qpl_active_flow_ids=431626709"]',}
			try:
				join=requests.post('https://www.facebook.com/api/graphql/',headers=headers,data=data).text
				if self.user_id in join:
					return True
				else:
					return join
			except:
				return False 
	def reac_cmt(self,id,type_react):
		access=''
		url=requests.get('https://mbasic.facebook.com/'+id,headers=self.headers,proxies='').url
		if id in url:
			return False
		index=1 if type_react=='LIKE' else 2 if type_react=='LOVE' else 3 if type_react=='CARE' else 4 if type_react=='HAHA' else 5 if type_react=='WOW' else 6 if type_react=='SAD' else 7
		access=requests.get(url,headers=self.headers).text
		while True:
			if id in access:
				find_cmt=access.split(id)[1].split('</a></span></span>')[0].split('/reactions/picker/?')[1].split('"')[0].replace('amp;','')
				access=requests.get('https://mbasic.facebook.com/reactions/picker/?'+find_cmt,headers=self.headers).text
				ufi=access.split('/ufi/reaction/?')
				hoan_thanh=requests.get('https://mbasic.facebook.com/ufi/reaction/?'+ufi[index].split('"')[0].replace('amp;',''),headers=self.headers).text
				return True
			else:
				if '/comment/replies/' in url:
					xemthemcmt=access.split('/comment/replies/?')[1].split('"')[0].replace('amp;','')
					access=requests.get('https://mbasic.facebook.com/comment/replies/?'+xemthemcmt,headers=self.headers).text
				else:
					xemthemcmt=access.split('/story.php?')[1].split('</a></div></div>')[0].replace('amp;','').split('"')[0]
					access=requests.get('https://mbasic.facebook.com/story.php?'+xemthemcmt,headers=self.headers).text
	def like(self,id,type):
		if '_' in id:
			uid=id.split('_')[1]
		else:
			uid=id
		list={'LIKE':1,'LOVE':2,'CARE':3,'HAHA':4,'WOW':5,'SAD':6,'ANGRY':7}
		headers={
		      'authority':'mbasic.facebook.com',
		      'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		      'content-type':'application/x-www-form-urlencoded',
		      'sec-ch-ua-mobile':'?0',
		      'sec-ch-ua-platform':'"Windows"',
		      'sec-fetch-dest':'document',
		      'sec-fetch-mode':'navigate',
		      'sec-fetch-site':'none',
		      'sec-fetch-user':'?1',
		      'upgrade-insecure-requests':'1',
		      'accept-language':'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3',
		      'cookie':self.cookie
}
		try:
			link='https://mbasic.facebook.com/reactions/picker/?ft_id='+uid
			data=requests.get(link,headers=self.headers).text
			get=data.split('<a href="')
			cx=get[list[type]].split('" style="display:block">')[0].replace('amp;','').replace(';','&')
			reac=requests.get('https://mbasic.facebook.com'+cx,headers=self.headers).text
			return True
		except:
			return False 
	def comment(self,id,msg):
		try:
			url=requests.get('https://mbasic.facebook.com/'+id,headers=self.headers).url
			access=requests.get(url,headers=self.headers).text
			cmt=re.findall('\/a\/comment.php\?fs=.*?"',access)
			if cmt==[]:return False
			hoan_thanh=requests.post('https://mbasic.facebook.com%s'%cmt[0].replace('"','').replace('amp;',''),headers=self.headers,data={'fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'comment_text':msg}).text
			return hoan_thanh
		except:
			return False
	def share(self,id,nd):
		try:
			url=requests.get('https://mbasic.facebook.com/'+id,headers=self.headers).url
			ac=requests.get(url,headers=self.headers).text
			node_share=re.findall('\/composer\/mbasic\/\?c_src=share.*?"',ac)
			if node_share==[]:
				return False
			truycapshare=ac.split('/composer/mbasic/?c_src=share')[1].split('"')[0].replace('amp;','')
			ac=requests.get('https://mbasic.facebook.com/composer/mbasic/?c_src=share'+truycapshare,headers=self.headers).text
			fb=ac.split('name="fb_dtsg" value="')[1].split('"')[0]
			jaz=ac.split('name="jazoest" value="')[1].split('"')[0]
			target=ac.split('name="target" value="')[1].split('"')[0]
			csid=ac.split('name="csid" value="')[1].split('"')[0]
			privacyx=ac.split('name="privacyx" value="')[1].split('"')[0]
			sid=ac.split('name="sid" value="')[1].split('"')[0]
			data={
			        'fb_dtsg':fb,
			         'jazoest':jaz,
			         'at':'',
			         'target':target,
			         'csid':csid,
			         'c_src':'share',
			         'referrer':'feed',
			         'ctype':'advanced',
			         'cver':'amber_share',
			         'users_with':'',
			         'album_id':'',
			         'waterfall_source':'advanced_composer_timeline',
			         'privacyx':privacyx,
			         'appid':'0',
			         'sid':sid,
			         'linkUrl':'',
			         'm':'self',
			         'xc_message':nd,
			         'view_post':'Chia sẻ',
			         'shared_from_post_id':sid,
			}
			share=ac.split('/composer/mbasic/?csid=')[2].split('"')[0].replace('amp;','')
			hoan_thanh=requests.post('https://mbasic.facebook.com/composer/mbasic/?csid='+share,headers=self.headers,data=data).text
			return True
		except:
			return False 
class TraoDoiSub_Api(object):
	def __init__(self,token):
		self.token=token
	def main(self):
		try:
			main=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+self.token).json()
			try:
				return main['data']
			except:
				False
		except:
			return False 
	def run(self,id):
		try:
			run=requests.get(f'https://traodoisub.com/api/?fields=run&id={id}&access_token={self.token}').json()
			try:
				run['data']['id']
				return True
			except:
				return False
		except:
			return False
	def get_job(self,type):
		try:
			get=requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={self.token}',headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'})
			return get
		except:
			return False 
	def nhan_xu(self,type,id):
		try:
			nhan=requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}',headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}).json()
			try:
				xu=nhan['data']['xu']
				msg=nhan['data']['msg']
				return msg,xu
			except:
				return nhan
		except:
			return False
class TuongTacCheo_Api(object):
	def __init__(self,token):
		self.token=token
	def login(self):
		try:
			log=requests.post('https://tuongtaccheo.com/logintoken.php',headers={'Content-type':'application/x-www-form-urlencoded',},data={'access_token':self.token})
			user=log.json()['data']['user']
			xu=log.json()['data']['sodu']
			self.cookie='PHPSESSID='+(log.cookies)['PHPSESSID']
			return user,xu
		except:
			try:print(log.json()['mess'])
			except:print(' Kiểm Tra Kết Nối Mạng (không đc sử dụng ip nước ngoài)')
			return False
	def run(self,id):
		data='iddat[]='+id+'&loai=fb'
		headers={
		 'Host':'tuongtaccheo.com',
		 'content-length':str(len(data)),
		 'accept':'*/*',
		 'origin':'https://tuongtaccheo.com',
		 'x-requested-with':'XMLHttpRequest',
		 'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
		 'referer':'https://tuongtaccheo.com/cauhinh/facebook.php',
		 'cookie':self.cookie
		}
		try:
			run=requests.post('https://tuongtaccheo.com/cauhinh/datnick.php',headers=headers,data=data).text
			if run=='1':
				return True
			else:
				return False 
		except:
			return False
	def getnv(self,type):
		headers={
		 'Host':'tuongtaccheo.com',
		 'accept':'application/json, text/javascript, *" . "/" . "*; q=0.01',
		 'x-requested-with':'XMLHttpRequest',
		 'user-agent':'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36',
		 'referer':'https://tuongtaccheo.com/kiemtien/',
		 'cookie':self.cookie
		}
		try:
			get=requests.post('https://tuongtaccheo.com/kiemtien'+type+'/getpost.php',headers=headers).json()
			return get
		except:
			return False
	def coin(self):
		headers={
		 'Host':'tuongtaccheo.com',
		 'x-requested-with':'XMLHttpRequest',
		 'user-agent':'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36',
		 'cookie':self.cookie
		}
		try:
			xu=requests.get('https://tuongtaccheo.com/home.php',headers=headers).text
			coin=xu.split('"soduchinh">')[1].split('<')[0]
			return coin
		except:
			return False
	def nhanxu(self,id,*type):
		data='id='+id if len(type)==1 else 'id='+id+'&loaicx='+type[1]
		url='https://tuongtaccheo.com/kiemtien'+type[0]+'/nhantien.php'
		headers={
		'Host':'tuongtaccheo.com',
		      'content-length':str(len(data)),
		      'x-requested-with':'XMLHttpRequest',
		      'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
		      'origin':'https://tuongtaccheo.com',
		      'referer':'https://tuongtaccheo.com/kiemtien'+type[0],
		      'cookie':self.cookie
		}
		try:
			nhan=requests.post(url,headers=headers,data=data).text
			return nhan
		except:
			return False 
	def nhanxu2(self,id,nv,type):
		if type==1:
			data='id='+id
		else:
			data='id='+id+'&loaicx='+type
		url='https://tuongtaccheo.com/kiemtien'+nv+'/nhantien.php'
		headers={
		'Host':'tuongtaccheo.com',
		      'content-length':str(len(data)),
		      'x-requested-with':'XMLHttpRequest',
		      'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
		      'origin':'https://tuongtaccheo.com',
		      'referer':'https://tuongtaccheo.com/kiemtien'+nv,
		      'cookie':self.cookie
		}
		try:
			nhan=requests.post(url,headers=headers,data=data).text
			return nhan
		except:
			return False
