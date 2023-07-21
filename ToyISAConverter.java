public class ToyISAConverter {
    private static String instructions;
    private static String rA;
    private static String rB;
    private static String op;
    private static String signed;
    private static int sign = 0;
    private static int icode;
    private static int pcPlusOne;

    private static String literal = "";

    public ToyISAConverter(String instructions) {
        this.instructions = instructions;
    }

    public static String convert() {
        if (instructions.equals("halt")) {
            return "90";
        }
        String[] instructList = instructions.split(" ");
        // 0 -> rA = rB
        // 1 -> rA += rB
        // 2 -> rA &= rB
        // 3 -> rA =@ rB (read from memory)
        // 4 -> rA @= rB (write to memory)
        // 5 ->
            // 0 -> rA ~= rA
            // 1 -> rA -= rA
            // 2 -> rA != rA
            // 3 -> rA .= pc
        // 6 ->
            // 0 -> rA == pc + 1
            // 1 -> rA +== pc + 1
            // 2 -> rA &== pc + 1
            // 3 -> rA ==@ pc + 1
        // 7 -> rA : rB  --(if rA <= 0 then jump to M[rB])
        // 8 ->
            // 0 -> rA -> rsp
            // 1 -> rA <- rsp
            // 2 -> pc+2 -> rsp, set pc = M[pc+1] (just 82)
            // 3 -> pc <- rsp

        op = instructList[1];
        rA = instructList[0];
        rB = instructList[2];
        if (!instructList[2].contains("r")) {
            pcPlusOne = Integer.parseInt(instructList[2]);
        }
        if (op.equals("->") || op.equals("<-")) {
            int b8 = 0;
            switch (op) {
                case "->" -> {
                    icode = 8;
                    if (!rA.contains("r")) {
                        b8 = 2;
                        rB = handlerB(getBinary(b8));
                        return handleOp(getBinary(icode)) + " " + "00" + rB;
                    }
                    else b8 = 0;
                }
                case "<-" -> {
                    icode = 8;
                    if (!rA.contains("r")){
                        b8 = 3;
                        rB = handlerB(getBinary(b8));
                        return handleOp(getBinary(icode)) + " " + "00" + rB;
                    }
                    else b8 = 1;
                }
            }
            int a = Integer.parseInt(String.valueOf(rA.charAt(1)));
            rA = handlerA(getBinary(a));
            rB = handlerB(getBinary(b8));
            op = handleOp(getBinary(icode));
            return op + " " + rA + rB + " " + literal;
        }

        int a = Integer.parseInt(String.valueOf(rA.charAt(1)));
        int b = Integer.parseInt(String.valueOf(rB.charAt(1)));

        switch (op) {
            case "=" -> icode = 0;
            case "+=" -> icode = 1;
            case "&=" -> icode = 2;
            case "=@" -> icode = 3;
            case "@=" -> icode = 4;
            case "~=" -> {
                icode = 5;
                b = 0;
            }
            case "-=" -> {
                icode = 5;
                b = 1;
            }
            case "!=" -> {
                icode = 5;
                b = 2;
            }
            case ".=" -> {
                icode = 5;
                b = 3;
            }
            case "==" -> {
                icode = 6;
                b = 0;
                literal += handlerB(Integer.toHexString(pcPlusOne));
            }
            case "+==" -> {
                icode = 6;
                b = 1;
                literal += handlerB(Integer.toHexString(pcPlusOne));
            }
            case "&==" -> {
                icode = 6;
                b = 2;
                literal += handlerB(Integer.toHexString(pcPlusOne));
            }
            case "==@" -> {
                icode = 6;
                b = 3;
                literal += handlerB(Integer.toHexString(pcPlusOne));
            }
            case ":" -> icode = 7;
            default -> throw new IllegalStateException("Unexpected value: " + op);
        }
        rA = handlerA(getBinary(a));
        rB = handlerB(getBinary(b));
        op = handleOp(getBinary(icode));
        return op + " " + rA + rB + " " + literal;
    }
    private static String getBinary(int value) {
        return Integer.toBinaryString(value);
    }
    private static String handleOp(String operation) {
        if (operation.length() < 4) {
            int zeroes = 4 - operation.length();
            while (zeroes > 0 ){
                operation = "0" + operation;
                zeroes--;
            }
        }
        return operation;
    }
    private static String handlerA(String registerA) {
        if (registerA.length() == 1) {
            registerA = "0" + registerA;
        }
        return registerA;
    }
    private static String handlerB(String registerB) {
        if (registerB.equals("0")) {
            registerB = registerB + "0";
        }
        return registerB;
    }


}
