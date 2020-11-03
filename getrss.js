var client = require('cheerio-httpcli');
var RSS = "http://news.yahoo.co.jp/pickup/computer/rss.xml";
var answer;
/*
client.fetch(RSS, {}, function(err, $, res) {
	if (err) { console.log("error"); return; }

	$("item > title").each(function(idx) {
				answer = $(this).text();
				//console.log(answer);
			});
	console.log("\n" + "RSSのタイトルを取得しました。");
})
*/
console.log('News: ' + answer);

function foo() {
	return new Promise((resolve, reject) => {
		client.fetch(RSS, {}, function(err, $, res) {
			if (err) { console.log("error"); return; }
		
			$("item > title").each(function(idx) {
						answer = $(this).text();
						console.log(answer);
					});
			console.log("\n" + "RSSのタイトルを取得しました。");
			resolve();
		});
	});
}

async function main() {
	try {
		await foo();
		console.log('matta');
	} catch (err) {
		console.log(err);
	}
}
main();