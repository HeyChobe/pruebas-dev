import styled from "styled-components";
import { useState } from "react";

const text = "la vaca lola, tiene cabeza y tiene cola";

const InputWrapper = styled.div`
  position: relative;
  height: 100px;
  width: 80%;
  margin: auto;
  margin-top: 20px;
  border-radius: 13px;
  overflow: hidden;

  -webkit-box-shadow: -1px 6px 7px 3px rgba(0, 0, 0, 0.61);
  box-shadow: -1px 6px 7px 3px rgba(0, 0, 0, 0.61);

  div {
    /* position: relative; */
    height: 100%;
    width: 50%;
    color: blue;
    float: right;
    margin: auto;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    font-size: 30px;
    /* background-color:red; */
    /* overflow-y: hidden; */
  }

  input {
    position: absolute;
    border: 0;
    height: 100%;
    width: 50%;
    border-radius: 13px;
    margin: auto;
    float: right;
    /* margin-top: -100px; */
    align-self: center;
    outline: none;
    background-color: transparent;
    font-size: 30px;
    padding-left: 50%;
  }
`;

function Input() {
  let arrayTextWords = [];
  let contArrayText = 0;
  let begin = 0;
  let final = 0;

  for (let i = 0; i <= text.length; i++) {
    if (i === text.length) {
      arrayTextWords[contArrayText] = text.slice(begin, final);
    }
    if (text[i] === " ") {
      arrayTextWords[contArrayText] = text.slice(begin, final);
      final = final + 1;
      begin = final;
      contArrayText++;
    } else {
      final = final + 1;
    }
  }
  console.log(arrayTextWords);

  //Hooks
  let [wordId, setWordId] = useState(0);
  let [letter, setLetter] = useState(0);
  let [del, setDel] = useState(false);

  //Retorna si la tecla presionada es delete
  const onKeyDown = (e) => {
    const code = e.which || e.keyCode;
    if(code===8){
        setDel(true);
    } else setDel(false);

    return del;
  }

  const onType = (e) => {
    console.log(e);
    const value = e.target.value;
    const length = value.length;
    const valueClean = value[length - 1];

    if (arrayTextWords[wordId]) {
      const word = arrayTextWords[wordId];

      //Si no presiona la tecla de borrar
      if(!del){
        if (word[letter] === valueClean) {
            console.log(`${word[letter]} " = " ${valueClean}`);
            setLetter(letter + 1);
          }
          else console.log(`${word[letter]} " != " ${valueClean}`);
    
          if (letter === word.length || valueClean === " ") {
              setLetter(0);
              setWordId(wordId + 1);
              console.log("Cambiando de palabra")
          }
      } else console.log("Borraste"); 
    }
  };

  return (
    <InputWrapper>
      <div>{text}</div>
      <input type='text' onKeyDown={onKeyDown} onChange={onType} />
    </InputWrapper>
  );
}

export default Input;
