#!/usr/bin/env python
# -*- coding: utf-8 -*-
import top.api
import json

#  http://www.alidayu.com/admin/service/tpl
 
req=top.api.AlibabaAliqinFcSmsNumSendRequest()
req.set_app_info(top.appinfo('23365309','42e6103da67067091d8996d4ad4b0c8b'))
 
req.extend = "11111111"
req.sms_type="normal"
req.sms_free_sign_name="身份验证"
params = {
    "code": "999999",
    "product": "节目名大类",
    "item": "具体节目"
}
#req.sms_param="{\"code\":\"888888\",\"product\":\"高端牛逼测试用例\"}"
req.sms_param = json.dumps(params)
req.rec_num="13410807370"
req.sms_template_code="SMS_7830147"
try:
    resp= req.getResponse()
    #jdata = json.loads(resp)
    #print(jdata)
    print resp
except Exception,e:
    print type(e)
    print(e)