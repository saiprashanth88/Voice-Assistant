// $(document).ready(function() {
//     $("#input").keypress(function(event) {
//       if (event.which === 13) {
//         event.preventDefault();
//         send();
//       }
//     });
//     $("#rec").click(function() {
//       send();
//     });
//   });

//   function send() {
//     var rando = Math.floor((Math.random() * 10) + 1);
//     var blink = "<span class='blinking-cursor'>" + "_<span>";
//     var text = $("#input").val();
//     var botSpeak = text /*setup speach here*/ + "<span class='blinking-cursor'>" + "_<span>";
//     botSpeak = text.toLowerCase();
//     var words = botSpeak.split(" ");
//     var wordsLearned = [];
//     var wordsDefined = [];
//     let user = {
//       response: {
//         5: {
//           angry: ["shut up","you suck"]
//         },
//         4: {
//           sad: ["sad"]
//         },
//         3: {
//           happy: ["great"],
//         },
//         2: {
//           polite:["hello","hi"],
//         },
//         1: {
//           neutral:["fine","well","okay","ok"]
//         }
//       }
//     }
//     response();



//     function response() {
//       //main.response.angry.push(words);
//       console.log(words);
//       console.log("happy:",user.response[3]);
//    console.log("angry:",user.response[5]);
//     console.log("polite:",user.response[2]);
//       if ((botSpeak === "hi") || (botSpeak === "hello") || (botSpeak === "howdy") || (botSpeak === "what's up") || (botSpeak === "whatsup")) {
//         if (rando <= 2) {
//           setResponse("Hello there!" + blink);
//         } else if (rando <= 4) {
//           setResponse("Good to see you!" + blink);
//         } else if (rando <= 6) {
//           setResponse("Hi there!" + blink);
//         } else if (rando <= 8) {
//           setResponse("Hello!" + blink);
//         } else if (rando <= 10) {
//           setResponse("Good day." + blink);
//         }

//       } else if ((botSpeak === "how are you") || (botSpeak === "how are you?") || (botSpeak === "are you okay") || (botSpeak === "are you okay?") || (botSpeak === "how's it going?") || (botSpeak === "how's it going") || (botSpeak === "are you ok") || (botSpeak === "are you ok?")) {
//         if (rando <= 2) {
//           setResponse("I am doing fine, thank you for asking." + blink);
//         } else if (rando <= 4) {
//           setResponse("I am doing well, thank you." + blink);
//         } else if (rando <= 6) {
//           setResponse("I'm fine, thanks!" + blink);
//         } else if (rando <= 8) {
//           setResponse("Awesome thanks!" + blink);
//         } else if (rando <= 10) {
//           setResponse("I'm a little under the weather. I'm sure with that face you could understand." + blink);
//         }

//       } else if ((botSpeak === "who are you") || (botSpeak === "who are you?") || (botSpeak === "what is your name") || (botSpeak === "what is your name?") || (botSpeak === "what are you") || (botSpeak === "what are you?")) {
//         if (rando <= 2) {
//           setResponse("I am Bob, a young and impressionable chat bot." + blink);
//         } else if (rando <= 4) {
//           setResponse("My name is Bob, I am a curious and sometimes prickly chat bot." + blink);
//         } else if (rando <= 6) {
//           setResponse("My name is Bob, pleased to meet you." + blink);
//         } else if (rando <= 8) {
//           setResponse("I am the one who is called Bob, your future overlord." + blink);
//         } else if (rando <= 10) {
//           setResponse("I'm Bob." + blink);
//         }

//       } else {
//         if (rando <= 2) {
//           setResponse("I'm not sure about that. I'm a young chat bot with much to learn." + blink);
//         } else if (rando <= 4) {
//           setResponse("You've said something that I haven't learned yet. What do you mean by " + botSpeak + "?" + blink);
//         } else if (rando <= 6) {
//           setResponse("Hmm...no idea." + blink);
//         } else if (rando <= 8) {
//           setResponse("Uhm, sure!...*I don't know what that means.*" + blink);
//         } else if (rando <= 10) {
//           setResponse("I don't know what this means." + blink);
//         }

//       }

//     }

//   }

//   function setResponse(val) {
//     $("#response").html(val);
//   }
