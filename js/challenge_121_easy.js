
var coin = process.argv[2];

console.log(run(parseInt(coin)));

function run(coin) {
  if(coin === 0) return 1;
  else return run(Math.floor(coin / 2)) + 
              run(Math.floor(coin / 3)) + 
              run(Math.floor(coin / 4));
}

