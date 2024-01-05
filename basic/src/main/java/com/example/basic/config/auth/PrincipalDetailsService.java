package com.example.basic.config.auth;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.example.basic.database.entity.WebEntity;
import com.example.basic.model.repository.WebRepository;

import lombok.extern.slf4j.Slf4j;

@Slf4j
@Service
public class PrincipalDetailsService implements UserDetailsService {

    @Autowired
    private WebRepository webRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        // TODO Auto-generated method stub
        log.info("[PrincipalDetailsService][loadUserByUsername] Start");
        log.info("Id : " + username);
        WebEntity user = webRepository.getUserDtoByUserId(username);
        // 이미 가입 된 사용자인지 확인
        if (user != null) {
            log.info("user : " + user.toString());
            return new PrincipalDetails(user);
        }
        return null;
    }

}
