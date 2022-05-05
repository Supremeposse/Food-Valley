import React from 'react';
import { Route, Switch } from 'react-router';
import Home from './containers/Home';

const Router = () => {
    return (
        <>
            <Switch>
                <Route exact path={'/twitter'} component={Home} />
            </Switch>
        </>
    );
};
export default Router;
