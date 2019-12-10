using UnityEngine;
using UnityEngine.UI;
using System;
public class UILogic : MonoBehaviour
{
    public Text text;
    public Text text2;
    public string processedText;
    public InputField input1;
    public InputField input2;
    public InputField input3;
    public InputField weight1;
    public InputField weight2;
    public InputField weight3;
    public float firstWeight;
    public float secondWeight;
    public float thirdWeight;
    public float totalWeight;
    public float totalGrade;


    public void getInput()
    {
        totalGrade = 0F;
        totalWeight = 0F;
        if(input1.text != "")
        {
            firstWeight = InputHandler.convertToFloat(weight1.text);
            totalWeight = totalWeight + firstWeight;
            totalGrade = totalGrade + (InputHandler.getAverage(input1.text)*firstWeight);
        }
        if (input2.text != "")
        {
            secondWeight = InputHandler.convertToFloat(weight2.text);
            totalWeight = totalWeight + secondWeight;
            totalGrade = totalGrade + (InputHandler.getAverage(input2.text) * secondWeight);
        }
        if (input3.text != "")
        {
            thirdWeight = InputHandler.convertToFloat(weight3.text);
            totalWeight = totalWeight + thirdWeight;
            totalGrade = totalGrade + (InputHandler.getAverage(input3.text) * thirdWeight);
        }
        totalGrade = totalGrade / totalWeight;
        displayOutput();
        //processText(input.textComponent.text);
    }
    public void displayOutput()
    {
        /*Debug.Log(processedText);
        string typeOfInput = "none";
        if (InputHandler.betterIsNum(processedText))
        {
            typeOfInput = "number";
        }
        else
        {
            typeOfInput = "string";
        }
        text.text = typeOfInput;*/
        //text.text = InputHandler.getAverageChars(processedText).ToString();
        text.text = totalGrade.ToString();
        if(totalGrade >= 70)
        {
            text2.text = "Don't worry";
        }
        else
        {
            text2.text = "Yes worry";
        }

    }
    public void processText(string inS)
    {
        Debug.Log("Before input handler: " + inS);
        //this.processedText = inS;
        this.processedText = InputHandler.processText(inS);
        displayOutput();
    }

}
