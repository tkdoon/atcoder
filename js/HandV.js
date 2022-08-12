// inputに入力データ全体が入る
function Main(input) {
    input = input.split("\n");
    var input0 = input[0]
    var H = parseInt(input0[0], 10);
    var W = parseInt(input0[1], 10);
    var K = parseInt(input0[2], 10);
    // 1行目がinput[0], 2行目がinput[1], …に入る

    for (let i = 1; i < H; i++) {
        input = input[i].split(" ");
        var c = []
        for (let j = 0; j < W; j++) {
            input[j] = parseInt(input[j], 10)
        }
        c[i] = input
    }
    //文字列から10進数に変換するときはparseIntを使います


    //出力
    console.log('%d %s', a + b + c, s);
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));