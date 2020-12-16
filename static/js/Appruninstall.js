var ios_starbucksUrl = "https://itunes.apple.com/kr/app/id466682252?mt=8";
var ios_ediyaUrl = "https://itunes.apple.com/kr/app/id378084485?mt=8";
var ios_gongchaUrl = "https://itunes.apple.com/kr/app/id378084485?mt=8";
var and_starbucksUrl = "https://play.google.com/store/apps/details?id=com.starbucks.co";
var and_ediyaUrl = "https://play.google.com/store/apps/details?id=com.sampleapp";
var and_gongchaUrl = "https://play.google.com/store/apps/details?id=com.sampleapp";

function runStarbucks_ios() {
  var clickedAt = +new Date();

  setTimeout(function () {
    if (+new Date() - clickedAt < 2000)
      if (window.confirm("스타벅스앱 최신 버전이 설치되어 있지 않습니다.\n설치페이지로 이동하시겠습니까?"))
        location.href = ios_starbucksUrl;
  }, 500);

  location.href = "starbucks://";
}

function runEdiya_ios() {
  var clickedAt = +new Date();

  setTimeout(function () {
    if (+new Date() - clickedAt < 2000)
      if (window.confirm("배달의 민족 최신 버전이 설치되어 있지 않습니다.\n설치페이지로 이동하시겠습니까?"))
        location.href = ios_ediyaUrl;
  }, 500);

  location.href = "smartbaedal://";
}

function runGongcha_ios() {
  var clickedAt = +new Date();

  setTimeout(function () {
    if (+new Date() - clickedAt < 2000)
      if (window.confirm("배달의 민족 최신 버전이 설치되어 있지 않습니다.\n설치페이지로 이동하시겠습니까?"))
        location.href = ios_gongchaUrl;
  }, 500);

  location.href = "smartbaedal://";
}


function runStarbucks_and() {
  var clickedAt = +new Date();

  setTimeout(function () {
    if (+new Date() - clickedAt < 2000)
      if (window.confirm("스타벅스앱 최신 버전이 설치되어 있지 않습니다.\n설치페이지로 이동하시겠습니까?"))
        location.href = and_starbucksUrl;
  }, 500);

  location.href = "starbucks://";
}

function runEdiya_and() {
  var clickedAt = +new Date();

  setTimeout(function () {
    if (+new Date() - clickedAt < 2000)
      if (window.confirm("배달의 민족 최신 버전이 설치되어 있지 않습니다.\n설치페이지로 이동하시겠습니까?"))
        location.href = and_ediyaUrl;
  }, 500);

  location.href = "smartbaedal://";
}

function runGongcha_and() {
  var clickedAt = +new Date();

  setTimeout(function () {
    if (+new Date() - clickedAt < 2000)
      if (window.confirm("배달의 민족 최신 버전이 설치되어 있지 않습니다.\n설치페이지로 이동하시겠습니까?"))
        location.href = and_gongchaUrl;
  }, 500);

  location.href = "smartbaedal://";
}
