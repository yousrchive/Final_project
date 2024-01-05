package com.example.basic.config.auth;

import java.util.ArrayList;
import java.util.Collection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import com.example.basic.database.entity.WebEntity;

import lombok.AllArgsConstructor;

// Spring Security가 이해할 수 있는 userDto는 UserDetails
// 우리가 만든 userDto를 Spring Security가 이해할 수 있는 UserDetils 만들어야함

@AllArgsConstructor
public class PrincipalDetails implements UserDetails {

    @Autowired
    private WebEntity WebEntity;

    // User의 권한
    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        // TODO Auto-generated method stub
        Collection<GrantedAuthority> collection = new ArrayList<>();
        collection.add(
                new GrantedAuthority() {
                    @Override
                    public String getAuthority() {
                        // userDto의 권한 추가
                        return WebEntity.getRole();
                    }
                });

        return collection;
    }

    @Override
    public String getPassword() {
        // TODO Auto-generated method stub
        return WebEntity.getPassword();
    }

    @Override
    public String getUsername() {
        // TODO Auto-generated method stub
        return WebEntity.getId();
    }

    @Override
    public boolean isAccountNonExpired() {
        // TODO Auto-generated method stub
        // 사용자 계정 만료 유무 확인
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        // TODO Auto-generated method stub
        // 계정 블록 유무 확인
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        // TODO Auto-generated method stub
        // 계정 비밀번호 오래 사용했는 지 확인
        return true;
    }

    @Override
    public boolean isEnabled() {
        // TODO Auto-generated method stub
        // 계정이 활성화 되어있는 지 확인
        return true;
    }

}
