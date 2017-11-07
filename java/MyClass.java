import java.io.System;

// Example for static field
public class MyClass {
    private static boolean staticField;
    private boolean instanceField;
    public static void main(String[] args){
        // a static method can access static fields
        staticField = true;

        // a static method can access instance field through an object reference
        MyClass mc = new MyClass();
        mc.instanceField = true;
    }
}

------------------------*--------------------------------
public class Hello
{
    // value / method
    public static String staticValue;
    public String nonStaticValue;
}

class A
{
    Hello hello = new Hello();
    hello.staticValue = "abc";
    hello.nonStaticValue = "xyz";
}

class B
{
    Hello hello2 = new Hello(); // here staticValue = "abc"
    hello2.staticValue; // will have value of "abc"
    hello2.nonStaticValue; // will have value of null
}
