from __future__ import print_function
import requests
import json

def send_alert(event, context):
	url = "https://open.larksuite.com/open-apis/bot/v2/hook/xxxxx-xxx-xxxx"
	lark_data = {
		"msg_type": "interactive",
		"card": {
			"config": {
				"wide_screen_mode": False, 
				"enable_forward": True
			},
			"elements": [{
				"tag": "div",
				"text": {
					"content": "<First line>",
					"tag": "lark_md"
				}
			}, {
				"tag": "div",
				"is_short":False,
				"text": {
					"content": "<Second line>",
					"tag": "lark_md"
				}
			}, {
				"tag": "div",
				"is_short":False,
				"text": {
					"content": "**<Third line with bold>**",
					"tag": "lark_md"
				}
			}, {
				"actions": [{
						"tag": "button",
						"text": {
							"content": "Button Here",
							"tag": "lark_md"
						},
						"url": "www.yourlink.com",
						"type": "danger"
				}],
				"tag": "action"
			}],
			"header": {
				"template": "orange",
				"title": {
					"content": "<Title Here>",
					"tag": "plain_text"
				}
			}
		}
	}

	response = requests.post(
		url, data=json.dumps(lark_data),
		headers={'Content-Type': 'application/json'}
	)

	try:
		output = response.json()
	except ValueError:
		output = response.text
	return output
