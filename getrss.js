var client = require('cheerio-httpcli');
var RSS = "http://news.yahoo.co.jp/pickup/computer/rss.xml";
var answer;

client.fetch(RSS, {}, function(err, $, res) {
	if (err) { console.log("error"); return; }

	$("item > title").each(function(idx) {
				answer = $(this).text();
				console.log(answer);
			});
	console.log("\n" + "RSSのタイトルを取得しました。");
})
