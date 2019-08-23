import requests
import codecs

#HEAD
p=requests.head(
	"http://teaching.bo-yuan.net/test/requests/"
)
print(p.text)

#GET
p=requests.get(
	"http://teaching.bo-yuan.net/test/requests/",
)
p.encoding="utf8"
print(p.text)

p=requests.get(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
	"action":"Go"
	}
)
p.encoding="utf8"
print(p.text)

#DELETE
p=requests.delete(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
	"action":"Go"
	},
	data="data content"
)
p.encoding="utf8"
print(p.text)

#DELETE
p=requests.delete(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
	"action":"Go"
	},
	data={
	"id":"test item"
	}
)
p.encoding="utf8"
print(p.text)

#PUT
p=requests.put(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
	"action":"Go"
	},
	data={
	"id":"test item"
	}
)
p.encoding="utf8"
print(p.text)

#PUT
p=requests.put(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
	"action":"Go"
	},
	data={
	"id":"test item","name":"myName"
	}
)
p.encoding="utf8"
print(p.text)

#PATCH
p=requests.patch(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
	"action":"Go"
	},
	data={
	"id":"test item","name":"myName"
	}
)
p.encoding="utf8"
print(p.text)

#PATCH
p=requests.patch(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
	"action":"Go"
	},
	data={
	"id":"test item","name":"myName","address":"myschool"
	}
)
p.encoding="utf8"
print(p.text)

#POST
p=requests.post(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
	"action":"Go"
	},
	data={
	"id":"test item","name":"myName","address":"myschool"
	}
)
p.encoding="utf8"
print(p.text)

