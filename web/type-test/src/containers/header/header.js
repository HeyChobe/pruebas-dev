import React from 'react';
import styled from 'styled-components';

const Header = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;

    h1{
        font-size: 50px;
        text-align: center;
    }
`;

const HeaderElements = styled.div`
    margin: auto;
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 70%; 

`;

function HeaderWrapper (){
    return(
        <Header>
            <h1>Type Test</h1>
            <HeaderElements>
                <div>Tiempo</div>
                <div>Cosas</div>
            </HeaderElements>
        </Header>
    );
}

export default HeaderWrapper;