package com.example.basic.service;

import com.example.basic.database.entity.WebEntity;

public interface WebService {
    public void joinUserDto(WebEntity entity);

    public void updateIsLoginByName(String name, Boolean isLogin);
}
