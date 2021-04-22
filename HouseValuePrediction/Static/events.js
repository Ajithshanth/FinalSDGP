        var input1_ = document.getElementById('n3');
        var input2_ = document.getElementById('n10');
        var answer = document.getElementById('n11');
        function sub(){
        n11.innerHTML = (parseInt(input1_.value) - parseInt(input2_.value));
        }
        var fun1 = document.getElementById("n3");
        var fun2 = document.getElementById("n10");

        fun1.addEventListener("keyup", function() {
           sub();
        });

        fun2.addEventListener("keyup", function() {
           sub();
        });

