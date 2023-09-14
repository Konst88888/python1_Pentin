# python1_Pentin
https://drive.google.com/drive/folders/1KOend6VHEZWyLJ-9WKsmtuCFk8Pb3MPL?usp=sharing   -- ссылка на JSON-коллекцию Postman и результат ее запуска


{
	"id": "df23faa7-c74e-4496-966b-355b84119448",
	"name": "Тестовое задание 1",
	"timestamp": "2023-09-14T10:22:26.489Z",
	"collection_id": "25413292-4fa85eed-1743-47bc-80ac-94f9733a698c",
	"folder_id": 0,
	"environment_id": "0",
	"totalPass": 8,
	"delay": 0,
	"persist": true,
	"status": "finished",
	"startedAt": "2023-09-14T10:22:22.726Z",
	"totalFail": 0,
	"results": [
		{
			"id": "6efe211f-b8fe-465e-924b-ea4590ea5f56",
			"name": "Создание",
			"url": "https://api.github.com/repos/Konst88888/python1_Pentin/issues",
			"time": 1258,
			"responseCode": {
				"code": 201,
				"name": "Created"
			},
			"tests": {
				"Body matches string": true,
				"Status code is 201": true
			},
			"testPassFailCounts": {
				"Body matches string": {
					"pass": 1,
					"fail": 0
				},
				"Status code is 201": {
					"pass": 1,
					"fail": 0
				}
			},
			"times": [
				1258
			],
			"allTests": [
				{
					"Body matches string": true,
					"Status code is 201": true
				}
			]
		},
		{
			"id": "13c4fc0b-212b-46bf-b1e5-a999e61dbadf",
			"name": "Получение списка",
			"url": "https://api.github.com/repos/Konst88888/python1_Pentin/issues",
			"time": 330,
			"responseCode": {
				"code": 200,
				"name": "OK"
			},
			"tests": {
				"Status code is 200": true,
				"Body matches string": true
			},
			"testPassFailCounts": {
				"Status code is 200": {
					"pass": 1,
					"fail": 0
				},
				"Body matches string": {
					"pass": 1,
					"fail": 0
				}
			},
			"times": [
				330
			],
			"allTests": [
				{
					"Status code is 200": true,
					"Body matches string": true
				}
			]
		},
		{
			"id": "b2eafbbb-4718-46a6-bd81-64d41e4e7d3d",
			"name": "Изменение",
			"url": "https://api.github.com/repos/Konst88888/python1_Pentin/issues/34",
			"time": 753,
			"responseCode": {
				"code": 200,
				"name": "OK"
			},
			"tests": {
				"Status code is 200": true,
				"Body matches string": true
			},
			"testPassFailCounts": {
				"Status code is 200": {
					"pass": 1,
					"fail": 0
				},
				"Body matches string": {
					"pass": 1,
					"fail": 0
				}
			},
			"times": [
				753
			],
			"allTests": [
				{
					"Status code is 200": true,
					"Body matches string": true
				}
			]
		},
		{
			"id": "546c330a-b2f4-4344-beb9-013463d5a535",
			"name": "Удаление",
			"url": "https://api.github.com/graphql",
			"time": 796,
			"responseCode": {
				"code": 200,
				"name": "OK"
			},
			"tests": {
				"Status code is 200": true,
				"Body matches string": true
			},
			"testPassFailCounts": {
				"Status code is 200": {
					"pass": 1,
					"fail": 0
				},
				"Body matches string": {
					"pass": 1,
					"fail": 0
				}
			},
			"times": [
				796
			],
			"allTests": [
				{
					"Status code is 200": true,
					"Body matches string": true
				}
			]
		}
	],
	"count": 1,
	"totalTime": 3137,
	"collection": {
		"requests": [
			{
				"id": "6efe211f-b8fe-465e-924b-ea4590ea5f56",
				"method": "POST"
			},
			{
				"id": "13c4fc0b-212b-46bf-b1e5-a999e61dbadf",
				"method": "GET"
			},
			{
				"id": "b2eafbbb-4718-46a6-bd81-64d41e4e7d3d",
				"method": "PATCH"
			},
			{
				"id": "546c330a-b2f4-4344-beb9-013463d5a535",
				"method": "POST"
			}
		]
	}
}
